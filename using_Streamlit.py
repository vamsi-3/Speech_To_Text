# import streamlit as st
# import speech_recognition as sr
# from datetime import datetime

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function to capture user's name via voice
# def get_user_name():
#     with sr.Microphone() as source:
#         st.info("🎤 Please say your name...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

#         try:
#             name = recognizer.recognize_google(audio)
#             st.success(f"✅ Detected Name: {name}")
#             return name
#         except Exception as e:
#             st.error(f"Error detecting name: {e}")
#             return None

# # Streamlit UI
# st.title("🎤 Speech-to-Text Transcriber")

# # Ask for user name by voice
# if "user_name" not in st.session_state:
#     if st.button("🎙️ Say Your Name"):
#         name = get_user_name()
#         if name:
#             st.session_state.user_name = name
#             st.success(f"Hello {name}! Your transcripts will be saved in {name}.txt")

# # Only proceed if name is captured
# if "user_name" in st.session_state:
#     file_name = f"{st.session_state.user_name}.txt"

#     # Upload audio file
#     uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

#     if uploaded_file:
#         with sr.AudioFile(uploaded_file) as source:
#             audio_data = recognizer.record(source)
#             st.info("Transcribing...")

#             try:
#                 text = recognizer.recognize_google(audio_data)

#                 # Show transcript
#                 st.success("✅ Transcription Complete!")
#                 st.write(text)

#                 # Add timestamp
#                 timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 entry = f"{text}  ({timestamp})\n"

#                 # Save transcript (append mode)
#                 with open(file_name, "a") as f:
#                     f.write(entry)

#                 # Download option
#                 with open(file_name, "r") as f:
#                     content = f.read()
#                 st.download_button("⬇️ Download Transcript", content, file_name=file_name)

#             except Exception as e:
#                 st.error(f"Error: {e}")
# import streamlit as st
# import speech_recognition as sr
# from datetime import datetime
# import uuid

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function to capture user's name via voice
# def get_user_name():
#     with sr.Microphone() as source:
#         st.info("🎤 Please say your name...")
#         recognizer.adjust_for_ambient_noise(source, duration=5)
#         audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

#         try:
#             name = recognizer.recognize_google(audio)
#             st.success(f"✅ Detected Name: {name}")
#             return name
#         except Exception as e:
#             st.error(f"Error detecting name: {e}")
#             return None

# # Function to transcribe speech (live mic or uploaded file)
# def transcribe_audio(audio_data, file_name):
#     try:
#         text = recognizer.recognize_google(audio_data)

#         # Show transcript
#         st.success("✅ Transcription Complete!")
#         st.write(text)

#         # Add timestamp
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         entry = f"{text}  ({timestamp})\n"

#         # Save transcript (append mode)
#         with open(file_name, "a") as f:
#             f.write(entry)

#         # Download option
#         with open(file_name, "r") as f:
#             content = f.read()
#         st.download_button("⬇️ Download Transcript", content, file_name=file_name)

#     except Exception as e:
#         st.error(f"Error: {e}")

# # Streamlit UI
# st.title("🎤 Speech-to-Text Transcriber")

# # Capture name if not already stored
# if "user_name" not in st.session_state:
#     if st.button("🎙️ Say Your Name"):
#         name = get_user_name()
#         if name:
#             # Generate unique ID using UUID
#             unique_id = uuid.uuid4().hex[:6]   # short unique ID
#             st.session_state.user_name = f"{name}_{unique_id}"
#             st.success(f"Hello {name}! Your transcripts will be saved in {st.session_state.user_name}.txt")

# # Only proceed if name is captured
# if "user_name" in st.session_state:
#     file_name = f"{st.session_state.user_name}.txt"

#     # Create two tabs: File Upload & Live Mic
#     tab1, tab2 = st.tabs(["📂 Upload Audio File", "🎙️ Live Recording"])

#     # TAB 1: File Upload
#     with tab1:
#         uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
#         if uploaded_file:
#             with sr.AudioFile(uploaded_file) as source:
#                 audio_data = recognizer.record(source)
#                 st.info("Transcribing uploaded file...")
#                 transcribe_audio(audio_data, file_name)

#     # TAB 2: Live Mic Recording
#     with tab2:
#         if st.button("🎤 Record Now"):
#             with sr.Microphone() as source:
#                 st.info("Listening... Please speak now.")
#                 recognizer.adjust_for_ambient_noise(source, duration=3)
#                 audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=20)
#                 st.info("Processing speech...")
#                 transcribe_audio(audio_data, file_name)
# import streamlit as st
# import speech_recognition as sr
# from datetime import datetime
# import uuid

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function: Capture user's name via voice
# def get_user_name(language):
#     with sr.Microphone() as source:
#         st.info("🎤 Please say your name...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
#             name = recognizer.recognize_google(audio, language=language)
#             st.success(f"✅ Detected Name: {name}")
#             return name
#         except sr.WaitTimeoutError:
#             st.error("⏳ You took too long to respond. Try again.")
#         except sr.UnknownValueError:
#             st.error("❌ Could not understand audio. Please try again in a quieter place.")
#         except sr.RequestError:
#             st.error("⚠️ Could not connect to speech recognition service.")
#         return None

# # Function: Transcribe speech with error handling
# def transcribe_audio(audio_data, file_name, language):
#     try:
#         text = recognizer.recognize_google(audio_data, language=language)

#         # Show transcript
#         st.success("✅ Transcription Complete!")
#         st.write(text)

#         # Add timestamp
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         entry = f"{text}  ({timestamp})\n"

#         # Save transcript
#         with open(file_name, "a",encoding ="utf-8") as f:
#             f.write(entry)

#         # Download option
#         with open(file_name, "r") as f:
#             content = f.read()
#         st.download_button("⬇️ Download Transcript", content, file_name=file_name)

#     except sr.UnknownValueError:
#         st.error("❌ Sorry, I could not understand the audio clearly.")
#     except sr.RequestError:
#         st.error("⚠️ API unavailable or network error.")
#     except Exception as e:
#         st.error(f"Unexpected Error: {e}")

# # Streamlit UI
# st.title("🎤 Speech-to-Text Transcriber")

# # Language selector
# language_map = {
#     "English": "en-US",
#     "Hindi": "hi-IN",
#     "Telugu": "te-IN",
#     "French": "fr-FR",
#     "Spanish": "es-ES"
# }
# language_choice = st.selectbox("🌍 Choose Language", list(language_map.keys()))
# language_code = language_map[language_choice]

# # Capture name if not already stored
# if "user_name" not in st.session_state:
#     if st.button("🎙️ Say Your Name"):
#         name = get_user_name(language_code)
#         if name:
#             unique_id = uuid.uuid4().hex[:6]
#             st.session_state.user_name = f"{name}_{unique_id}"
#             st.success(f"Hello {name}! Your transcripts will be saved in {st.session_state.user_name}.txt")

# # Only proceed if name is captured
# if "user_name" in st.session_state:
#     file_name = f"{st.session_state.user_name}.txt"

#     # Tabs for File Upload & Live Mic
#     tab1, tab2 = st.tabs(["📂 Upload Audio File", "🎙️ Live Recording"])

#     # TAB 1: File Upload
#     with tab1:
#         uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
#         if uploaded_file:
#             with sr.AudioFile(uploaded_file) as source:
#                 audio_data = recognizer.record(source)
#                 st.info("Transcribing uploaded file...")
#                 transcribe_audio(audio_data, file_name, language_code)

#     # TAB 2: Live Mic Recording
#     with tab2:
#         if st.button("🎤 Record Now"):
#             with sr.Microphone() as source:
#                 st.info("Listening... Please speak now.")
#                 recognizer.adjust_for_ambient_noise(source, duration=1)
#                 try:
#                     audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=10)
#                     st.info("Processing speech...")
#                     transcribe_audio(audio_data, file_name, language_code)
#                 except sr.WaitTimeoutError:
#                    st.error("⏳ No speech detected within the time limit. Try again.")
import streamlit as st
import speech_recognition as sr
from datetime import datetime
import uuid
from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Initialize recognizer
recognizer = sr.Recognizer()

# Function: Capture user's name via voice
def get_user_name(language):
    with sr.Microphone() as source:
        st.info("🎤 Please say your name...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            name = recognizer.recognize_google(audio, language=language)
            st.success(f"✅ Detected Name: {name}")
            return name
        except Exception as e:
            st.error(f"Error detecting name: {e}")
            return None

# Function: Save transcript in multiple formats
def save_transcript(text, file_name, file_choice):
    if file_choice == "Text File (.txt)":
        final_name = file_name + ".txt"
        with open(final_name, "w", encoding="utf-8") as f:
            f.write(text)
        return final_name

    elif file_choice == "Word File (.docx)":
        final_name = file_name + ".docx"
        doc = Document()
        doc.add_paragraph(text)
        doc.save(final_name)
        return final_name

    elif file_choice == "PDF File (.pdf)":
        final_name = file_name + ".pdf"
        styles = getSampleStyleSheet()
        pdf = SimpleDocTemplate(final_name)
        pdf.build([Paragraph(text, styles["Normal"])])
        return final_name

# Function: Transcribe audio with error handling
def transcribe_audio(audio_data, file_name, language):
    try:
        text = recognizer.recognize_google(audio_data, language=language)

        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{text}  ({timestamp})\n"

        # Store transcript in session state (so it persists!)
        st.session_state.transcript = entry

        st.success("✅ Transcription Complete!")
        st.write(entry)

    except sr.UnknownValueError:
        st.error("❌ Could not understand audio.")
    except sr.RequestError:
        st.error("⚠️ Could not connect to Google API.")
    except Exception as e:
        st.error(f"Unexpected Error: {e}")

# Streamlit UI
st.title("🎤 AI Speech-to-Text Transcriber")

# Language selector
language_map = {
    "English": "en-US",
    "Hindi": "hi-IN",
    "Telugu": "te-IN",
    "French": "fr-FR",
    "Spanish": "es-ES"
}
language_choice = st.selectbox("🌍 Choose Language", list(language_map.keys()))
language_code = language_map[language_choice]

# Ask for name
if "user_name" not in st.session_state:
    if st.button("🎙️ Say Your Name"):
        name = get_user_name(language_code)
        if name:
            unique_id = uuid.uuid4().hex[:6]
            st.session_state.user_name = f"{name}_{unique_id}"
            st.success(f"Hello {name}! Your transcripts will be saved as {st.session_state.user_name}.txt/.docx/.pdf")

# Continue if name captured
if "user_name" in st.session_state:
    file_name = st.session_state.user_name

    # Two tabs for options
    tab1, tab2 = st.tabs(["📂 Upload Audio File", "🎙️ Live Recording"])

    # TAB 1: Upload File
    with tab1:
        uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
        if uploaded_file:
            with sr.AudioFile(uploaded_file) as source:
                audio_data = recognizer.record(source)
                st.info("Transcribing uploaded file...")
                transcribe_audio(audio_data, file_name, language_code)

    # TAB 2: Live Recording
    with tab2:
        if st.button("🎤 Record Now"):
            with sr.Microphone() as source:
                st.info("Listening... Please speak now.")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                try:
                    audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                    st.info("Processing speech...")
                    transcribe_audio(audio_data, file_name, language_code)
                except sr.WaitTimeoutError:
                    st.error("⏳ No speech detected. Try again.")

    # ✅ File format + download stays even after rerun
    if "transcript" in st.session_state:
        st.markdown("---")
        st.subheader("📥 Save & Download Transcript")

        file_choice = st.selectbox(
            "Choose file type",
            ["Text File (.txt)", "Word File (.docx)", "PDF File (.pdf)"],
            key="file_choice"
        )

        saved_file = save_transcript(st.session_state.transcript, file_name, file_choice)

        if file_choice == "Text File (.txt)":
            with open(saved_file, "r", encoding="utf-8") as f:
                st.download_button("⬇️ Download TXT", f.read(), file_name=saved_file)

        elif file_choice == "Word File (.docx)":
            with open(saved_file, "rb") as f:
                st.download_button("⬇️ Download DOCX", f, file_name=saved_file)

        elif file_choice == "PDF File (.pdf)":
            with open(saved_file, "rb") as f:
                st.download_button("⬇️ Download PDF", f, file_name=saved_file)
