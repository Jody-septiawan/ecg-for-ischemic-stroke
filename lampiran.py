from flask import (Flask, render_template, request, redirect,
                   url_for, flash, Response, jsonify, make_response, send_file)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy.orm import load_only
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure
from biosppy.signals import ecg
from statistics import mean
from statistics import stdev
from sklearn.neighbors import KNeighborsClassifier
import math
import io
import random
import os
import pymysql
import pandas as pd
import numpy as np
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = "SangatSangatRahasia"

dbhost = 'localhost:8889'
dbuser = 'root'
dbpass = 'root'
dbname = 'sinyal'

conn = "mysql://{0}:{1}@{2}/{3}".format(dbuser, dbpass, dbhost, dbname)

app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Hasil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(10))
    jml_puncak = db.Column(db.Integer)
    jml_data = db.Column(db.Integer)
    meanrr = db.Column(db.Float)
    sdrr = db.Column(db.Float)
    cvrr = db.Column(db.Float)
    rmssd = db.Column(db.Float)
    label = db.Column(db.Integer)
    status = db.Column(db.String(10))
    proses = db.Column(db.Integer)
    is_active = db.Column(db.Integer)
    over = db.Column(db.Integer)

    def __init__(self, subject, jml_puncak, jml_data, meanrr, sdrr, cvrr, rmssd, label, status, proses, is_active, over):

        self.subject = subject
        self.jml_puncak = jml_puncak
        self.jml_data = jml_data
        self.meanrr = meanrr
        self.sdrr = sdrr
        self.cvrr = cvrr
        self.rmssd = rmssd
        self.label = label
        self.status = status
        self.proses = proses
        self.is_active = is_active
        self.over = over


class Takurasi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nilai_k = db.Column(db.Integer)
    akurasi = db.Column(db.Float)

    def __init__(self, id, nilai_k, akurasi):
        self.id = id
        self.nilai_k = nilai_k
        self.akurasi = akurasi


class Akurasi_subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(10))
    target = db.Column(db.Integer)
    prediksi = db.Column(db.Integer)
    nilai_k = db.Column(db.Integer)

    def __init__(self, subject, target, prediksi, nilai_k):
        self.subject = subject
        self.target = target
        self.prediksi = prediksi
        self.nilai_k = nilai_k

@app.route('/')
def Index():
    Hasil_1 = Hasil.query.filter(
        (Hasil.label == 1) & (Hasil.status == 'latih') & (Hasil.is_active == 1))

    Hasil_1_over = Hasil.query.filter(
        (Hasil.label == 1) & (Hasil.status == 'latih') & (Hasil.over == 1))

    Hasil_0 = Hasil.query.filter(
        (Hasil.label == 0) & (Hasil.status == 'latih') & (Hasil.is_active == 1))

    Hasil_0_over = Hasil.query.filter(
        (Hasil.label == 0) & (Hasil.status == 'latih') & (Hasil.over == 1))

    proses = Hasil.query.filter((Hasil.status == 'latih') &
                                (Hasil.proses == 0) & (Hasil.is_active == 1)).count()

    jml_stroke = {'1': Hasil_1.count()+Hasil_1_over.count(),
                  '0': Hasil_0.count()+Hasil_0_over.count()}

    return render_template("latih.html", Hasil_1=Hasil_1, Hasil_0=Hasil_0, Hasil_0_over=Hasil_0_over, Hasil_1_over=Hasil_1_over, proses=proses, title='latih', jml_stroke=jml_stroke)


@app.route('/shw-uji-subject')
def shw_uji_subject():
    data = Akurasi_subject.query.order_by(
        desc('id')).group_by(Akurasi_subject.subject)

    Hasil_1 = Hasil.query.filter(
        (Hasil.label == 1) & (Hasil.status == 'uji') & (Hasil.is_active == 1))
    Hasil_0 = Hasil.query.filter(
        (Hasil.label == 0) & (Hasil.status == 'uji') & (Hasil.is_active == 1))

    dAkurasi = Takurasi.query.order_by(desc('akurasi'))

    val_acc = 0
    val_accu = 0
    val_pres = 0
    val_sens = 0
    benar = 0
    len_data = 0
    tp = 0
    fp = 0
    fn = 0
    tn = 0

    for i in data:
        len_data += 1

        if i.target == 1:
            if i.target == i.prediksi:
                tp += 1
            else:
                fn += 1
        else:
            if i.target == i.prediksi:
                tn += 1
            else:
                fp += 1

        if i.prediksi == i.target:
            benar += 1

    if len_data != 0:
        val_acc = round((benar/len_data)*100, 2)

        if tp != 0:
            val_accu = round(((tp+tn)/(tp+tn+fp+fn))*100, 2)

            val_pres = round(((tp)/(tp+fp))*100, 2)

            val_sens = round((tp)/(tp+fn)*100, 2)

    # confusion matrix

    cmatrix = {'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn,
               'acc': val_accu, 'pres': val_pres, 'sens': val_sens}

    # return render_template('coba.html', data=cmatrix)

    return render_template('uji_subject.html', data=data, title='pengujian', Hasil_1=Hasil_1, Hasil_0=Hasil_0, dAkurasi=dAkurasi, val_acc=val_acc, cmatrix=cmatrix)


@app.route('/delete-uji-subject')
def delete_uji_subject():
    Akurasi_subject.query.delete()
    db.session.commit()

    return redirect(url_for('shw_uji_subject'))


@app.route('/delete-akurasi-k')
def delete_akurasi_k():
    Takurasi.query.delete()
    db.session.commit()

    return redirect(url_for('shw_uji_subject'))


def proses_uji_subject_by_id(id_subject, nilai_k):
    fields = ['subject', 'cvrr', 'rmssd', 'label']
    dLatih = Hasil.query.filter(
        Hasil.status == 'latih').options(load_only(*fields))

    dataL = []
    target = []
    for i in dLatih:
        dataL.append([i.cvrr, i.rmssd])
        # dataL.append([i.meanrr, i.sdrr, i.cvrr, i.rmssd])
        target.append(i.label)

    my_data = Hasil.query.get(id_subject)

    knn = KNeighborsClassifier(n_neighbors=nilai_k)
    knn.fit(dataL, target)
    temp_subject_uji = [
        [my_data.cvrr, my_data.rmssd]]
    prediksi = knn.predict(temp_subject_uji)

    data_ku = Akurasi_subject(
        my_data.subject, my_data.label, prediksi[0], nilai_k)
    db.session.add(data_ku)
    db.session.commit()


@app.route('/uji_subject', methods=['POST'])
def uji_subject():
    if request.method == 'POST':
        id_subject = int(request.form['id_subject'])
        nilai_k = int(request.form['nilai_k'])

        tHasil = Hasil.query.filter(
            (Hasil.status == 'uji') & (Hasil.is_active == 1) & (Hasil.proses == 1))

        if id_subject == 0:
            for t in tHasil:
                proses_uji_subject_by_id(t.id, nilai_k)

        else:
            proses_uji_subject_by_id(id_subject, nilai_k)

    return redirect(url_for('shw_uji_subject'))


@app.route('/akurasi')
def Akurasi():
    Takurasi.query.delete()
    db.session.commit()

    dHasil = Hasil.query.filter(
        (Hasil.proses == 1) & (Hasil.status == 'latih') & (Hasil.is_active == 1))

    fields = ['subject', 'meanrr', 'sdrr', 'cvrr', 'rmssd', 'label']
    dLatih = Hasil.query.filter((
        Hasil.status == 'latih') & (Hasil.is_active == 1)).options(load_only(*fields))

    dUji = Hasil.query.filter((
        Hasil.status == 'uji') & (Hasil.is_active == 1)).options(load_only(*fields))

    dataU = []
    targetU = []
    for i in dUji:
        dataU.append([i.cvrr, i.rmssd])
        targetU.append(i.label)

    dataL = []
    target = []
    for i in dLatih:
        dataL.append([i.cvrr, i.rmssd])
        target.append(i.label)

    nk = []
    for k in range(len(dataL)):
        knn = KNeighborsClassifier(n_neighbors=k+1)
        knn.fit(dataL, target)

        benar = 0
        for j in range(len(dataU)):
            temp_data_uji = [dataU[j]]
            prediksi = knn.predict(temp_data_uji)
            prediksi = prediksi[0]
            if targetU[j] == prediksi:
                benar += 1

        akurasi = round((benar/len(dataU))*100, 2)
        my_data = Takurasi(k+1, k+1, akurasi)
        db.session.add(my_data)
        db.session.commit()

    flash("Akurasi done", "akurasi")

    return redirect(url_for('shw_uji_subject'))


@app.route('/uji')
def Uji():
    Hasil_1 = Hasil.query.filter(
        (Hasil.label == 1) & (Hasil.status == 'uji') & (Hasil.is_active == 1))

    Hasil_1_over = Hasil.query.filter(
        (Hasil.label == 1) & (Hasil.status == 'uji') & (Hasil.over == 1))

    Hasil_0 = Hasil.query.filter(
        (Hasil.label == 0) & (Hasil.status == 'uji') & (Hasil.is_active == 1))

    Hasil_0_over = Hasil.query.filter(
        (Hasil.label == 0) & (Hasil.status == 'uji') & (Hasil.over == 1))

    proses = Hasil.query.filter((Hasil.status == 'uji') &
                                (Hasil.proses == 0) & (Hasil.is_active == 1)).count()

    jml_stroke = {'1': Hasil_1.count()+Hasil_1_over.count(),
                  '0': Hasil_0.count()+Hasil_0_over.count()}

    dAkurasi = Takurasi.query.order_by(desc('akurasi'))

    return render_template("uji.html", Hasil_1=Hasil_1, Hasil_0=Hasil_0, proses=proses, title='data uji', dAkurasi=dAkurasi, jml_stroke=jml_stroke)


@app.route('/grafik/<subject>')
def Grafik(subject):

    return render_template('grafik.html', subject=subject)


# INSERT
ALLOWED_EXTENSION = set(['png', 'jpeg', 'jpg', 'csv'])
app.config['UPLOAD_FOLDER'] = 'uploads'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION


@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':

        file = request.files['file']
        alamat = request.form['url']

        if 'file' not in request.files:
            return redirect(url_for(alamat))

        if file.filename == '':
            flash('Tidak ada file yang dipilih', 'success')
            return redirect(url_for(alamat))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = filename[:5]+'.csv'.lower()
            a = os.listdir('uploads/')
            a = [a.lower() for a in a]

            if filename not in a:
                path = app.config['UPLOAD_FOLDER']
                file.save(os.path.join(path, filename))
            else:
                data = 'uploads/'+filename

                flash("Subject "+filename[:5]+" sudah ada")

                return redirect(url_for('Index'))

                # os.remove(data)

        subject = filename[:5]
        jml_puncak = 0
        jml_data = 0
        meanrr = 0
        sdrr = 0
        cvrr = 0
        rmssd = 0
        label = request.form['label']
        status = alamat
        proses = 0
        is_active = 1
        over = 0

        my_data = Hasil(subject, jml_puncak, jml_data,
                        meanrr, sdrr, cvrr, rmssd, label, status, proses, is_active, hover)
        db.session.add(my_data)
        db.session.commit()

        flash("File berhasil disimpan")

    return redirect(url_for('Index'))


@app.route("/reset_by", methods=['POST'])
def reset_by():
    if request.method == 'POST':

        id_subject = request.form['id_subject']
        url = request.form['url']

        my_data = Hasil.query.get(id_subject)
        my_data.meanrr = 0
        my_data.sdrr = 0
        my_data.cvrr = 0
        my_data.rmssd = 0
        my_data.proses = 0
        db.session.commit()

        if url == 'latih':
            return redirect(url_for('Index'))
        elif url == 'uji':
            return redirect(url_for('Uji'))


@app.route("/matplot-as-image-<subject>.svg")
def plot_svg(subject):
    signal = np.loadtxt('uploads/'+subject+'.csv')
    signal = signal[:10000]

    _, _, r_peaks, _, _, _, _ = ecg.ecg(
        signal=signal, sampling_rate=500, show=False)

    fig = Figure(figsize=(12, 4))
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(signal)
    axis.plot(r_peaks, signal[r_peaks], 'r*')
    axis.grid()

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


def to_dict(row):
    if row is None:
        return None

    rtn_dict = dict()
    keys = row.__table__.columns.keys()
    for key in keys:
        rtn_dict[key] = getattr(row, key)
    return rtn_dict


@app.route("/excel")
def exportexcel():
    data = Takurasi.query.all()
    data_list = [to_dict(item) for item in data]
    df = pd.DataFrame(data_list)
    filename = app.config['UPLOAD_FOLDER']+"/autos.xlsx"
    print("Filename: "+filename)

    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, sheet_name='Akurasi')
    writer.save()

    return send_file(filename)


@app.route("/proses_data/<status>")
def proses_data(status):

    def read_signal(subject):
        return np.loadtxt('uploads/'+subject+'.csv')

    def puncak_r(unfiltered_ecg, p_fs):
        _, _, r_peaks, _, _, _, _ = ecg.ecg(
            signal=unfiltered_ecg, sampling_rate=p_fs, show=False)

        return r_peaks

    def koevar(sd, mean):
        return sd/mean*100

    def root_mean_square_sd(rr_interval):
        temp = []
        for i in range(len(rr_interval)):
            if(i != len(rr_interval)-1):
                temp.append(pow(rr_interval[i]-rr_interval[i+1], 2))

        return math.sqrt((1/(len(rr_interval)-1))*sum(temp))

    dataa = Hasil.query.filter((Hasil.status == status) & (Hasil.proses == 0))
    if dataa.count() == 0:
        flash("Semua data sudah diproses", "alldone")

    temp = []
    for i in dataa:
        unfiltered_ecg = read_signal(i.subject)
        r_peaks = puncak_r(unfiltered_ecg, 500)
        rr_interval = np.diff(r_peaks)

        # Ekstraksi Ciri Sintal EKG
        meanrr = mean(rr_interval)
        sdrr = stdev(rr_interval)
        cvrr = koevar(sdrr, meanrr)
        rmssd = root_mean_square_sd(rr_interval)

        my_data = Hasil.query.get(i.id)
        my_data.meanrr = meanrr
        my_data.sdrr = sdrr
        my_data.cvrr = cvrr
        my_data.rmssd = rmssd
        my_data.proses = 1
        db.session.commit()

    if status == 'latih':
        return redirect(url_for('Index'))
    elif status == 'uji':
        return redirect(url_for('Uji'))
