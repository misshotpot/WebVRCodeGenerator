import streamlit.components.v1 as components  # Import Streamlit
import streamlit as st

st.title('Hospital VR Training Simulator')
st.write('Click VR to enter the hospital training environment and scroll down to see generated code 🏥')

col1, col2, col3 = st.columns((1,1,2))

# 医院相关物品
Options = ["hospital-bed","medical-cart","examination-table","wheelchair","medicine-cabinet","iv-stand","stretcher","waiting-chair","nurses-station"]
choose = st.sidebar.selectbox("Pick a hospital object:", Options)

Options2 = [" ","ambient","point"]
choose2 = st.sidebar.selectbox("Want some lights:", Options2)

# 医院环境
Options3 = [" ","hospital-room","emergency-room","waiting-area","operating-room","patient-ward","clinic-room","icu-room","laboratory"]
choose3 = st.sidebar.selectbox("Choose Hospital Environment:", Options3)

Options4 = ["no","yes"]
choose4 = st.sidebar.selectbox("Want fog:", Options4)


def writeHelp1():
    st.write('Corresponding Code:')
    st.header("Generated Code:")
    st.write('<html><head>')
    st.write('<script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>')
    st.write('<script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>')
    st.write('<script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script>')
    st.write('</head><body>')
    st.write('<a-scene>')
    
    
    
def writeHelp2():
    st.write('</a-scene>')
    st.write('</body></html>')  


if st.sidebar.button('Generate Hospital VR Scene'):

    fog = '<a-scene fog="type: exponential; color: #E8F4F8"></a-scene>'

    if choose == "hospital-bed":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box position="-1 0.5 -3" rotation="0 0 0" color="#FFFFFF" width="2" height="0.5" depth="1"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light> <a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box position="-1 0.5 -3" rotation="0 0 0" color="#FFFFFF" width="2" height="0.5" depth="1"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light> <a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-box position="-1 0.5 -3" rotation="0 0 0" color="#FFFFFF" width="2" height="0.5" depth="1"></a-box>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
       
        
    if choose == "medical-cart":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box position="-1 0.5 -3" rotation="0 0 0" color="#C0C0C0" width="0.8" height="1" depth="0.5"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box position="-1 0.5 -3" rotation="0 0 0" color="#C0C0C0" width="0.8" height="1" depth="0.5"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-box position="-1 0.5 -3" rotation="0 0 0" color="#C0C0C0" width="0.8" height="1" depth="0.5"></a-box>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
        
    if choose == "examination-table":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box position="-1 0.5 -3" rotation="0 0 0" color="#D3D3D3" width="1.5" height="0.8" depth="0.7"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)    
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box position="-1 0.5 -3" rotation="0 0 0" color="#D3D3D3" width="1.5" height="0.8" depth="0.7"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-box position="-1 0.5 -3" rotation="0 0 0" color="#D3D3D3" width="1.5" height="0.8" depth="0.7"></a-box>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "wheelchair":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-cylinder position="-1 0.5 -3" rotation="90 0 0" color="#4A4A4A" height="0.8" radius="0.3"></a-cylinder><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>'+fog+'</a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-cylinder position="-1 0.5 -3" rotation="90 0 0" color="#4A4A4A" height="0.8" radius="0.3"></a-cylinder><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-cylinder position="-1 0.5 -3" rotation="90 0 0" color="#4A4A4A" height="0.8" radius="0.3"></a-cylinder>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "medicine-cabinet":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box color="#FFFFFF" width="1.2" height="1.5" depth="0.3" position = "-1 1 -3"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)    
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box color="#FFFFFF" width="1.2" height="1.5" depth="0.3" position = "-1 1 -3"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-box color="#FFFFFF" width="1.2" height="1.5" depth="0.3" position = "-1 1 -3"></a-box>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "iv-stand":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-cylinder color="#808080" height="2" radius="0.05" position="-1 1 -3"></a-cylinder><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross">'+fog+'</a-entity></a-scene></body></html>', width=600, height=300)
        else:    
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-cylinder color="#808080" height="2" radius="0.05" position="-1 1 -3"></a-cylinder><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-cylinder color="#808080" height="2" radius="0.05" position="-1 1 -3"></a-cylinder>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "stretcher":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box color="#FFD700" width="2" height="0.3" depth="0.8" position="-1 0.5 -3"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>'+fog+'</a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box color="#FFD700" width="2" height="0.3" depth="0.8" position="-1 0.5 -3"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-box color="#FFD700" width="2" height="0.3" depth="0.8" position="-1 0.5 -3"></a-box>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        writeHelp2()
    
    if choose == "waiting-chair":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box color="#4169E1" width="0.6" height="0.8" depth="0.6" position = "-1 0.4 -3"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>'+fog+'</a-scene></body></html>', width=600, height=300)
        else:
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box color="#4169E1" width="0.6" height="0.8" depth="0.6" position = "-1 0.4 -3"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-box color="#4169E1" width="0.6" height="0.8" depth="0.6" position = "-1 0.4 -3"></a-box>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
    
    if choose == "nurses-station":
        if choose4 == "yes":
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box color="#8B4513" width="1.5" height="1" depth="0.8" position = "-3 0.5 -3"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>'+fog+'</a-scene></body></html>', width=600, height=300)
        else:    
            components.html('<html><head><script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script><script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script><script src="https://unpkg.com/aframe-event-set-component@4.2.1/dist/aframe-event-set-component.min.js"></script></head><body><a-scene><a-box color="#8B4513" width="1.5" height="1" depth="0.8" position = "-3 0.5 -3"></a-box><a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light><a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity></a-scene></body></html>', width=600, height=300)
        writeHelp1()
        st.write('<a-box color="#8B4513" width="1.5" height="1" depth="0.8" position = "-3 0.5 -3"></a-box>')
        st.write('<a-light type='+choose2+' color="#F0F0F0" position="0 5 0"></a-light>')
        st.write('<a-entity environment="preset: '+choose3+'; groundColor: #E8F4F8; grid: cross"></a-entity>')
        if choose4 == "yes":
            st.write(fog)
        writeHelp2()
