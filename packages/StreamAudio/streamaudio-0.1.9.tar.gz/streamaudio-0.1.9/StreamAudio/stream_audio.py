import pyaudio
import threading

class AudioStreamer:
    """
    A class for streaming audio from the microphone.
    """

    def __init__(self, format=pyaudio.paInt16, channels=1, rate=16000, chunk=1024):
        """
        Initializes the audio streamer with the given audio settings.

        :param format: Audio format (default is 16-bit int)
        :param channels: Number of audio channels (default is 1)
        :param rate: Sampling rate in Hz (default is 16000)
        :param chunk: Buffer size for each audio read (default is 1024)
        """
        self.format = format
        self.channels = channels
        self.rate = rate
        self.chunk = chunk

        self.audio_interface = pyaudio.PyAudio()
        self.stream = None

        self.stop_event = threading.Event()
        self.audio_thread = None

    def start_streaming(self):
        """
        Starts the audio stream.
        """
        try:
            self.stream = self.audio_interface.open(format=self.format,
                                                    channels=self.channels,
                                                    rate=self.rate,
                                                    input=True,
                                                    frames_per_buffer=self.chunk)
            self.stop_event.clear()
            self.audio_thread = threading.Thread(target=self._stream_audio)
            self.audio_thread.start()
            print("Audio streaming started...")
        except Exception as e:
            print(f"Error starting audio stream: {e}")
            self.stop_streaming()

    def stop_streaming(self):
        """
        Stops the audio stream and cleans up resources.
        """
        self.stop_event.set()
        if self.audio_thread:
            self.audio_thread.join()
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio_interface.terminate()
        print("Audio stream stopped.")

    def _stream_audio(self):
        """
        Internal method that continuously streams audio from the microphone.
        """
        try:
            while not self.stop_event.is_set():
                data = self.stream.read(self.chunk, exception_on_overflow=False)
                # This is where the streamed audio data is available
                # You can process the audio data here if needed
                print("Audio chunk captured")  # This is just a placeholder for now
        except Exception as e:
            print(f"Error during audio streaming: {e}")
            self.stop_streaming()
        finally:
            print("Audio streaming stopped.")

# Usage
if __name__ == "__main__":
    streamer = AudioStreamer()
    try:
        streamer.start_streaming()
        while True:
            pass  # Keep the app running
    except KeyboardInterrupt:
        print("Stopping audio stream...")
        streamer.stop_streaming()
