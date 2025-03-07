# ######## Import the required packages ############
# import streamlit as st
# import google.generativeai as genai

# ####### Provide your API key ###################
# api_key = "your api key"
# genai.configure(api_key=api_key)

# ######## Choose the heading ###############
# st.header("Text Summarization")

# ########## Text input ##################
# text_input = st.text_area("Enter the text to summarize")

# ######### Use genai skill ##########################
# if st.button("GET SUMMARY"):
#     if text_input:
#         # Adding a directive for summarization
#         prompt = f"Please summarize the following text:\n\n{text_input}"
#         model = genai.GenerativeModel("gemini-1.0-pro")  # Ensure this model supports summarization
#         response = model.generate_content([prompt])
        
#         # Displaying the summary
#         st.markdown("### Summary:")
#         st.write(response.text.strip())
#     else:
#         st.warning("Please enter some text to summarize.")


# import streamlit as st
# import assemblyai as aai
# import tempfile
# from collections import Counter
# import re
# import google.generativeai as genai

# # Set the AssemblyAI API key
# aai.settings.api_key = "your_api key"

# # Set the Google Generative AI API key
# genai.configure(api_key="your api key")

# # Streamlit app title and description
# st.title("Audio Transcription and Text-Based Report Generation App")
# st.write("Upload an MP3 file to transcribe the audio and generate a report based on the transcribed text.")
# st.write("You can also summarize the transcription below.")

# # Upload audio file
# uploaded_file = st.file_uploader("Upload an MP3 file", type="mp3")

# def generate_report(text):
#     # Simple text-based analysis to extract themes and key sections
#     sentences = text.split('\n')
    
#     # Count keywords
#     word_list = re.findall(r'\b\w+\b', text.lower())
#     word_counts = Counter(word_list)
#     common_words = word_counts.most_common(5)
    
#     # Extract themes based on frequent keywords
#     themes = ", ".join([word for word, count in common_words if len(word) > 3])
    
#     # Prepare sections
#     intro = "This report provides an overview of the key points discussed in the audio transcription."
#     discussion_points = "\n".join(sentences[:5])  # Display first few lines as main discussion points
#     speaker_contributions = "This audio featured multiple speakers contributing their perspectives."
#     conclusion = "The key themes in this discussion include: " + themes

#     # Form the report
#     report_text = f"""
#     **Generated Report**

#     **Introduction**
#     {intro}

#     **Main Discussion Points**
#     {discussion_points}

#     **Speaker Contributions**
#     {speaker_contributions}

#     **Conclusion**
#     {conclusion}
#     """
    
#     return report_text

# if uploaded_file:
#     # Save the uploaded file to a temporary location
#     with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#         temp_file.write(uploaded_file.read())
#         temp_file_path = temp_file.name
    
#     # Configure transcription with speaker labels
#     config = aai.TranscriptionConfig(
#         speaker_labels=True,
#         speakers_expected=2
#     )

#     # Transcribe the audio
#     st.write("Transcribing audio...")
#     transcript = aai.Transcriber().transcribe(temp_file_path, config)

#     # Display the transcript with speaker labels
#     full_text = ''
#     for utterance in transcript.utterances:
#         full_text += f"Speaker {utterance.speaker}: {utterance.text}\n"
#     st.text_area("Transcript", full_text, height=300)

#     # Generate Report button
#     if st.button("Generate Report"):
#         # Generate report based on transcript text
#         report_text = generate_report(full_text)
        
#         # Display report and enable download
#         st.text_area("Generated Report", report_text, height=300)

#         # Download report as a text file
#         st.download_button(
#             label="Download Report",
#             data=report_text,
#             file_name="generated_report.txt",
#             mime="text/plain"
#         )

#     # Text summarization using the generated transcript
#     st.header("Text Summarization")
    
#     ######### Use genai skill for summarization ##########################
#     if st.button("GET SUMMARY"):
#         if full_text:
#             # Adding a directive for summarization
#             prompt = f"Please summarize the following text:\n\n{full_text}"
#             model = genai.GenerativeModel("gemini-1.0-pro")  # Ensure this model supports summarization
#             response = model.generate_content([prompt])
            
#             # Displaying the summary
#             st.markdown("### Summary:")
#             st.write(response.text.strip())
#         else:
#             st.warning("No transcript available to summarize.")


import streamlit as st
import assemblyai as aai
import tempfile
from collections import Counter
import re
import google.generativeai as genai

# Set the AssemblyAI API key
aai.settings.api_key = "f1179f53109b4527928593df904db8e3"

# Set the Google Generative AI API key
genai.configure(api_key="AIzaSyBlOq7ZMhNV1Ry4aL_2dHQuBInQn3loDlo")

# Streamlit app title and description
st.title("Audio Transcription and Text-Based Report Generation App")
st.write("Upload an MP3 file to transcribe the audio and generate a report based on the transcribed text.")
st.write("You can also summarize the transcription below.")

# Upload audio file
uploaded_file = st.file_uploader("Upload an MP3 file", type="mp3")

def generate_report(text, summary):
    # Simple text-based analysis to extract themes and key sections
    sentences = text.split('\n')
    
    # Count keywords
    word_list = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(word_list)
    common_words = word_counts.most_common(5)
    
    # Extract themes based on frequent keywords
    themes = ", ".join([word for word, count in common_words if len(word) > 3])
    
    # Prepare sections
    intro = "This report provides an overview of the key points discussed in the audio transcription."
    discussion_points = summary  # Use the summary text as discussion points
    speaker_contributions = "This audio featured multiple speakers contributing their perspectives."
    conclusion = "The key themes in this discussion include: " + themes

    # Form the report
    report_text = f"""
    **Generated Report**

    **Introduction**
    {intro}

    **Main Discussion Points**
    {discussion_points}

    **Speaker Contributions**
    {speaker_contributions}

    **Conclusion**
    {conclusion}
    """
    
    return report_text

if uploaded_file:
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    
    # Configure transcription with speaker labels
    config = aai.TranscriptionConfig(
        speaker_labels=True,
        speakers_expected=2
    )

    # Transcribe the audio
    st.write("Transcribing audio...")
    transcript = aai.Transcriber().transcribe(temp_file_path, config)

    # Display the transcript with speaker labels
    full_text = ''
    for utterance in transcript.utterances:
        full_text += f"Speaker {utterance.speaker}: {utterance.text}\n"
    st.text_area("Transcript", full_text, height=300)

    # Text summarization using the generated transcript
    st.header("Text Summarization")
    
    ######### Use genai skill for summarization ##########################
    if st.button("GET SUMMARY"):
        if full_text:
            # Adding a directive for summarization
            prompt = f"Please summarize the following text:\n\n{full_text}"
            model = genai.GenerativeModel("gemini-1.0-pro")  # Ensure this model supports summarization
            response = model.generate_content([prompt])
            
            # Displaying the summary
            st.markdown("### Summary:")
            summary_text = response.text.strip()
            st.write(summary_text)

            # Generate report based on transcript text for download
            report_text = generate_report(full_text, summary_text)

            # Enable download button for the report
            st.text_area("Generated Report", report_text, height=300)
            st.download_button(
                label="Download Report",
                data=report_text,
                file_name="generated_report.txt",
                mime="text/plain"
            )
        else:
            st.warning("No transcript available to summarize.")


