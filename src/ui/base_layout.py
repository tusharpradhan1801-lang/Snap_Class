import streamlit as st 


def style_background_home():
    st.markdown("""
        <style> 
            .stApp{
                background:#EBE9E1 !important ;
                }

         .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>
                """
                ,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style> 
            .stApp{
                background:#EBE9E1 !important ;
                }

         .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>
                """
                ,unsafe_allow_html=True)


def style_base_deshboard():
    st.markdown("""
        <style> 
            .stApp{
                background:#EBE9E1 !important ;
                }
        </style>
                """
                ,unsafe_allow_html=True)
    
    
def style_base_layout():
    st.markdown("""
        <style> 
        @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400..700;1,400..700&family=Petit+Formal+Script&display=swap');

         /* hide top Bar of streamlit */
         #MainMenu ,footer ,header{
          visibility: hidden ;
         }
         .block-container{
           padding-top:1.5rem !important ;

         }
            .stApp{
                background:#EBE9E1 !important ;
                }

        h1 {
          font-family: "Libre Baskerville", serif !important;
                 font-size:3rem !important;
         font-style: normal !important;
         line-height:1.1 !important ;
         margin-bottom:0rem !important;
         color: #E43D12 !important;
         
        }
     .petit-formal-script-regular {
         font-family: "Petit Formal Script", cursive;
         font-weight: 500;
         font-style: normal;
         }


        h2 {
                font-family: "Libre Baskerville", serif !important;
             font-size:2rem !important;
             font-style:normal !important;
                 line-height:1.1 !important ;
                 margin-bottom:0rem !important;
                        color: #E43D12 !important;
                 
          }
        h3,h4,p {
         font-family: "Petit Formal Script", cursive;
        color: #E43D12 !important;
          }

        button[kind="primary"]{
                background: #EBE9E1!important;
               border-radius:1.5rem !important;
                color:#EBE9E1 !important;
                padding: 10px 20px !important;
             border: none !important;
                transition: transform 0.25s ease-in-out !important;
                  }
        
        button[kind="secondary"]{
        background: #EBE9E1 !important;
        border-radius:1.5rem !important;
        color:#E43D12 !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: transform 0.25s ease-in-out !important;
          }

        button[kind="tertiary"]{
                background:#EBE9E1 !important;
          border-radius:1.5rem !important;
                color:#E43D12 !important;
                padding: 10px 20px !important;
          border: none !important;
                transition: transform 0.25s ease-in-out !important;
                  }

        button:hover{
        transform: scale(1.05)
        }
        </style>
                """
                ,unsafe_allow_html=True)

     