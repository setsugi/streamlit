import streamlit as st
from PIL import Image


# タイトル表示
st.title('自己紹介')

st.write('Streamlitの勉強も兼ねて簡単な自己紹介ページ作りました。')

st.header('趣味')

hobby_expander = st.beta_expander('詳細はこちら', expanded=False)
with hobby_expander:
    st.subheader('ゲーム')
    st.write('フォートナイト')
    st.subheader("動画視聴")
    st.write('YouTube Netflix')
    st.subheader('バイク')
    st.write('所有バイク：G310R')
    # 画像の表示
    img = Image.open('g310r.jpg')
    st.image(img, caption='g310r', use_column_width=True)

st.header('プログラミング')

programming_expander = st.beta_expander('詳細はこちら', expanded=False)
with programming_expander:
    st.subheader('好きな言語')
    st.write('Python')
    st.subheader("今後勉強していきたい言語")
    st.write('Python, JavaScript, Rust')
    st.subheader('フレームワーク')
    st.write('Django, Streamlit勉強中')

st.header('目標')

the_goal_expander = st.beta_expander('詳細はこちら', expanded=False)
with the_goal_expander:
    st.subheader('資格取得')
    st.write('基本情報技術者試験の合格を目指す')
    st.subheader('プログラミング')
    st.write('''
        Paiza  
        Aランクの問題クリアを目指す（現在2021/04/22はBランク）
    ''')
