import streamlit as st

st.set_page_config(layout="wide")
st.markdown("""
<style>
.big-font {
    font-size: 40px !important;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font"> KUALITAS UDARA PADA PROVINSI DKI JAKARTA </p>', unsafe_allow_html=True)

st.subheader('Peta DKI Jakarta')

colu1, colu2 = st.columns([4, 1])
with colu1:
    import folium
    from streamlit_folium import st_folium
    m = folium.Map(location=[-6.241586, 106.992416], zoom_start=11)
    icon1 = folium.Icon(color="darkblue")
    icon2 = folium.Icon(color="red")
    icon3 = folium.Icon(color="purple")
    icon4 = folium.Icon(color="green")
    icon5 = folium.Icon(color="orange")
    folium.Marker(
        [-6.195322117029913, 106.82310195807386], popup="UDARA : TIDAK SEHAT", 
        tooltip="Bundaran HI",
        icon=icon1
    ).add_to(m)
    folium.Marker(
        [-6.1528630832227655, 106.89343818072786], popup="UDARA : TIDAK SEHAT", 
        tooltip="Kelapa gading",
        icon=icon2
    ).add_to(m)
    folium.Marker(
        [-6.331951542862599, 106.81439116568198], popup="UDARA : TIDAK SEHAT", 
        tooltip="Jagakarsa",
        icon=icon3
    ).add_to(m)
    folium.Marker(
        [-6.291030482700883, 106.89962883811985], popup="UDARA : TIDAK SEHAT", 
        tooltip="Lubang Buaya",
        icon=icon4
    ).add_to(m)
    folium.Marker(
        [-6.195942, 106.773595], popup="UDARA : TIDAK SEHAT", 
        tooltip="Kebon Jeruk",
        icon=icon5
    ).add_to(m)
    
    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=1360, height=500)

with colu2:
   st.subheader('Keterangan Lokasi Tower')
   colo1, colo2 = st.columns([0.8, 4.2])
   with colo1:
      from PIL import Image
      #
      image = Image.open('b.png')
      resized_image = image.resize((35, 35))
      st.image(resized_image)
      #
      image = Image.open('m.png')
      resized_image = image.resize((35, 35))
      st.image(resized_image)
      #
      image = Image.open('u.png')
      resized_image = image.resize((35, 35))
      st.image(resized_image)
      #
      image = Image.open('h.png')
      resized_image = image.resize((35, 35))
      st.image(resized_image)
      #
      image = Image.open('o.png')
      resized_image = image.resize((35, 35))
      st.image(resized_image)
   with colo2:
      st.write("DKI 1 Bunderan HI")
      st.write("DKI 2 Kelapa Gading")
      st.write("DKI 3 Jagakarsa")
      st.write("DKI 4 Lubang Buaya")
      st.write("DKI 5 Kebon Jeruk")
      


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   st.write("""
   <h2 style="font-size: 24px;
   text-align:center;
   background-color:green;
   ">Baik
   </h2>""", unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 12px;
   color:black;
   text-align:center;
   background-color:white;
   ">Tingkat kualitas udara yang sangat baik, tidak memberikan efek negatif terhadap manusia, hewan, tumbuhan.
   </h2>""", unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 16px;
   font-weight:bold;
   color:black;
   text-align:center;
   background-color:white;
   ">Apa yang harus dilakukan:
   </h2>""", unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 12px;
   color:black;
   text-align:center;
   background-color:white;
   ">Sangat baik melakukan kegiatan diluar.
   </h2>""", unsafe_allow_html=True)
   st.image("https://static.streamlit.io/examples/owl.jpg")

with col2:
   st.write('<h2 style="font-size: 24px;text-align:center;background-color:blue;">Sedang</h2>', unsafe_allow_html=True)
   st.write('<h2 style="font-size: 12px;color:black;text-align:center;background-color:white;">Tingkat kualitas udara masih dapat diterima pada kesehatan manusia, hewan dan tumbuhan..</h2>', unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 16px;
   font-weight:bold;
   color:black;
   text-align:center;
   background-color:white;
   ">Apa yang harus dilakukan:
   </h2>""", unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 12px;
   color:black;
   text-align:center;
   background-color:white;
   ">Kelompok sensitif : Kurangi aktivitas fisik yang terlalu lama atau berat. Setiap orang : Masih dapat beraktivitas di luar.
   </h2>""", unsafe_allow_html=True)
   st.image("https://static.streamlit.io/examples/owl.jpg")

with col3:
   st.write('<h2 style="font-size: 24px;text-align:center;background-color:orange;">Tidak Sehat</h2>', unsafe_allow_html=True)
   st.write('<h2 style="font-size: 12px;color:black;text-align:center;background-color:white;">Tingkat kualitas udara yang bersifat merugikan paga manusia, hewan, dan tumbuhan.</h2>', unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 16px;
   font-weight:bold;
   color:black;
   text-align:center;
   background-color:white;
   ">Apa yang harus dilakukan:
   </h2>""", unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 12px;
   color:black;
   text-align:center;
   background-color:white;
   ">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
   </h2>""", unsafe_allow_html=True)
   st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
   st.write('<h2 style="font-size: 24px;text-align:center;background-color:red;">Sangat Tidak Sehat</h2>', unsafe_allow_html=True)
   st.write('<h2 style="font-size: 12px;color:black;text-align:center;background-color:white;">Tingkat kualitas udara yang dapat meningkatkan resiko kesehatan pada sejumlah segmen populasi yang terpapar.</h2>', unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 16px;
   font-weight:bold;
   color:black;
   text-align:center;
   background-color:white;
   ">Apa yang harus dilakukan:
   </h2>""", unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 12px;
   color:black;
   text-align:center;
   background-color:white;
   ">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
   </h2>""", unsafe_allow_html=True)
   st.image("https://static.streamlit.io/examples/owl.jpg")

with col5:
   st.write('<h2 style="font-size: 24px;text-align:center;background-color:black;">Berbahaya</h2>', unsafe_allow_html=True)
   st.write('<h2 style="font-size: 12px;color:black;text-align:center;background-color:white;">Tingkat kualitas udara yang dapat merugikan kesehatan serius pada populasi dan perlu penanganan cepat.</h2>', unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 16px;
   font-weight:bold;
   color:black;
   text-align:center;
   background-color:white;
   ">Apa yang harus dilakukan:
   </h2>""", unsafe_allow_html=True)
   st.write("""
   <h2 style="font-size: 12px;
   color:black;
   text-align:center;
   background-color:white;
   ">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
   </h2>""", unsafe_allow_html=True)
   st.image("https://static.streamlit.io/examples/owl.jpg")


from PIL import Image
image = Image.open('ui.png')
resized_image = image.resize((150, 150))
st.sidebar.image(resized_image)

st.sidebar.markdown("# Pengaturan Visualisasi")
import datetime
import streamlit as st

add_selectbox = st.sidebar.selectbox(
    'Pilih Lokasi',
    ('DKI 1 Bunderan HI', 'DKI 2 Kelapa Gading', 'DKI 3 Jagakarsa','DKI 4 Lubang Buaya', 'DKI 5 Kebon Jeruk')
)
st.sidebar.markdown("# Pengaturan")

st.sidebar.date_input(
    "Tanggal",
    datetime.date(2020, 2, 20))

add_selectbox = st.sidebar.selectbox(
    'Metode',
    ('Extreme Learning Machine', 'Kernel Extreme Learning Machine')
)
