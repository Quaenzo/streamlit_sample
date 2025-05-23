import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import pandas as pd 
df = pd.read_csv('users.csv')

users = { 'usernames' : {}}

for _, row in df.iterrows():
    username = row['username']
    users['usernames'][username] = {
        'name' : row['name'],
        'password' : row['password'],
        'email' : row['email'],
        'failed_login_attemps' : row['failed_login_attemps'],
        'logged_in' : row['logged_in'],
        'role' : row['role']
    }
authenticator = Authenticate(
    users,
    'cookie name',
    'cookie key',
    30,
)

authenticator.login()

def accueil():
    st.title('Bienvenue sur ma page')
    st.image('https://www.focus.it/images/2022/02/03/applauso_1020x680.jpg')


if st.session_state['authentication_status']:
    
    authenticator.logout('Deconnexion', location='sidebar')
    st.sidebar.write(f"Bienvenue {st.session_state['username']}")
    with st.sidebar:
        selection = option_menu(
            menu_title=None,
            options=['Accueil', 'Photos'],
            icons=['house','camera'],
            orientation='vertical')
    if selection == 'Accueil':
            accueil()
    elif selection == 'Photos':
            st.title("Bienvenue dans mon album de photos de cute animaux")
            col1, col2, col3 = st.columns(3)
            with col1: 
                st.image('https://images.ctfassets.net/cnu0m8re1exe/c175AfE5netP1i6bvd5tc/84a983d021f09be04717afa9374b4473/red_panda_lead.jpg?fm=jpg&fl=progressive&w=660&h=433&fit=fill')
            with col2:
                st.image('https://mymodernmet.com/wp/wp-content/uploads/2019/12/felted-animals-yulia-derevschikova-7.jpg')
            with col3:
                st.image('https://media.cnn.com/api/v1/images/stellar/prod/180813120103-animals-cats-cute-45170cat-stock-photo.jpg?q=x_16,y_0,h_1334,w_2370,c_crop/h_833,w_1480')
    
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')