import streamlit as st
from streamlit.runtime.scriptrunner import RerunException, RerunData

def rerun():
    raise RerunException(RerunData())

lyrics = [
    {
        "text": """Ooh, I just love the way you've got me feelin' (oh, you got me feelin') 
In love with the feelin' (oh, you got me feelin')
It's like, ooh
Take away the pain, baby, I'm healin' (baby, I'm healin')
Baby, I'm healin' (baby, I'm healin', yeah, yeah, yeah, yeah, yeah)
I don't need anything more (oh, oh)
Be the wave, I'll be the shore (shore, oh)
Crashing all over me, I want you (oh, oh, oh, oh, oh)""",
        "title": "Feel It"
    },
    {
        "text": """You're taking me out of the ordinary
I want you laying me down
Till we're dead and buried
On the edge of your knife
Staying drunk on your vine
The angels up in the clouds
Are jealous knowing we found
Something so out of the ordinary
You got me kissing the ground of your sanctuary
Shatter me with your touch
Oh, Lord, return me to dust
The angels up in the clouds
Are jealous knowing we found""",
        "title": "Ordinary"
    },
    {
        "text": """When I close my eyes
It's you there in my mind""",
        "title": "8 Letters"
    },
    {
        "text": """I'm a skeleton when you say my name
And the high, no, it never goes away
Like jumpin' out an airplane to swimmin' with the sharks
That existential feelin' when you're starin' at the stars
There's a hurricane in my head, but the lightnin' in my heart
Makes it worth it
Yeah, I still get nervous""",
        "title": "Nervous"
    }
]

st.set_page_config(page_title="Just Feel It", page_icon="💖", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF69B4;'> 🎵 Just Feel It 🎵</h1>", unsafe_allow_html=True)

if "started" not in st.session_state:
    st.session_state.started = False
if "index" not in st.session_state:
    st.session_state.index = 0

# Centralizando o conteúdo usando um div com estilo CSS
with st.container():
    st.markdown(
        """
        <style>
            .centered-content {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
            .btn-centered > button {
                background-color: #FF69B4;
                color: white;
                font-size: 18px;
                padding: 10px 25px;
                border-radius: 10px;
                border: none;
                cursor: pointer;
                margin-top: 20px;
                transition: background-color 0.3s ease;
            }
            .btn-centered > button:hover {
                background-color: #ff85c1;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<div class='centered-content'>", unsafe_allow_html=True)
    
    if not st.session_state.started:
        if st.button("Clique aqui para iniciar sua jornada", key="start_button"):
            st.session_state.started = True
            rerun()
    else:
        current = lyrics[st.session_state.index]
        st.markdown(f"<h3>{current['title']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:18px; font-style: italic;'>{current['text'].replace(chr(10), '<br>')}</p>", unsafe_allow_html=True)

        if st.button("Mostrar próximo trecho ▶️", key="next_button"):
            st.session_state.index = (st.session_state.index + 1) % len(lyrics)
            rerun()

    st.markdown("</div>", unsafe_allow_html=True)
