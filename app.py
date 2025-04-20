import streamlit as st
from PIL import Image
import requests
import json
import streamlit_lottie

# Set page configuration
st.set_page_config(page_title="Saad Qamar | Portfolio", layout="wide")

# Load profile image
profile_image = Image.open("saad.jpeg")

# Load Lottie animation
lottie_url = "https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json"  # AI-themed animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottie_url(lottie_url)

# Background and styles
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    }
    .big-font {
        font-size: 70px !important;
        font-weight: bold;
        color: white;
        text-shadow: 0px 0px 10px #00ffe7;
    }
    .project-card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        margin-bottom: 2rem;
    }
    .form {
        background-color: rgba(0,0,0,0.3);
        padding: 20px;
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_image, width=300)
with col2:
    st.markdown("<div class='big-font'>Hi, I'm Saad Qamar</div>", unsafe_allow_html=True)
    st.write("""
    Passionate Freelancer tech enthusiast offering innovative digital solutions and support. 
    """)
    streamlit_lottie.st_lottie(lottie_animation, speed=1, loop=True, height=200, key="ai")

# About
st.markdown("## 🙋‍♂️ About Me")
st.write("""
I'm a tech enthusiast with a strong passion for development, cybersecurity, AI, and automation.  
I provide professional services and solutions across these domains, helping clients build secure, smart, and scalable systems.

Whether it's automating workflows, building secure applications, or integrating AI into products —  
I love solving real-world problems through technology.
""")

st.markdown("## 🧠 Skills and Services")
st.markdown("""
- 🔧 **Web Development** — Modern websites and web apps using Django, Streamlit, and Tailwind CSS  
- 🤖 **Python Automation** — Task automation, script development, and system integrations  
- 🌐 **Web Scraping** — Data extraction and API integrations for insights and automation  
- 🔒 **Cybersecurity Services** — SOC setup, security monitoring (Wazuh), and DevSecOps practices  
- 🧩 **CI/CD & DevOps** — Docker, Git, CircleCI, Terraform, Kubernetes for streamlined deployments  
- 🛍️ **E-commerce Solutions** — Custom online stores with payment integration and product management  
- 🎨 **UI/UX Design Support** — Clean, responsive, and user-friendly interfaces  
""")

# Projects
st.markdown("## 🗂️ Projects")
with open("projects.json") as f:
    projects = json.load(f)

cols = st.columns(3)
for index, project in enumerate(projects):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="project-card">
            <h4>{project['title']}</h4>
            <p>{project['description']}</p>
            <a href="{project['github']}" target="_blank">GitHub</a>
        </div>
        """, unsafe_allow_html=True)


# Contact Form (Formsubmit.io)
st.markdown("## ☎ Contact Me")
st.markdown("""
<form action="https://formsubmit.co/saadqamar213569@gmail.com" method="POST" class="form">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required style="width:100%; padding:10px; margin-bottom:10px;">
    <input type="email" name="email" placeholder="Your email" required style="width:100%; padding:10px; margin-bottom:10px;">
    <textarea name="message" placeholder="Your message here..." required style="width:100%; padding:10px; margin-bottom:10px;"></textarea>
    <button type="submit" style="padding:10px 20px; background-color:#00ffe7; border:none; border-radius:5px; cursor:pointer;">Send ✉️</button>
</form>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
---
<center>Made with ❤️ by Saad Qamar</center>
""", unsafe_allow_html=True)