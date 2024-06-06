from services.gong_service import get_mp4_feed, get_email_feed
from services.transcription_service.py import transcribe_audio
from services.llm_service import summarize, classify, infer, generate_business_points
from utils.data_utils import save_transcript

def main():
    # Fetch MP4 and email feeds
    mp4_feed = get_mp4_feed()
    email_feed = get_email_feed()

    # Assume we are transcribing the first MP4 from the feed
    mp4_url = mp4_feed['data'][0]['url']
    transcript = transcribe_audio(mp4_url)
    save_transcript(transcript)

    # LLM processing
    summary = summarize(transcript)
    classification = classify(transcript)
    inference = infer(transcript)
    business_points = generate_business_points(transcript)

    # Print the results
    print("Summary:", summary)
    print("Classification:", classification)
    print("Inference:", inference)
    print("Business Points:", business_points)

if __name__ == '__main__':
    main()

