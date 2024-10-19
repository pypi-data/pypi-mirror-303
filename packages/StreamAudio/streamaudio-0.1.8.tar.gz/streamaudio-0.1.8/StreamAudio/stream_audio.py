import pyaudio
import threading
import wave
from queue import Queue, Empty

class AudioStreamer:
    """
    A class for streaming audio from the microphone and processing it in real time.
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

        self.callbacks = []
        self.stop_event = threading.Event()
        self.audio_thread = None
        self.audio_queue = Queue()
        self.frames = []

    def start_streaming(self):
        """
        Starts the audio stream and begins processing audio data.
        """
        self.stream = self.audio_interface.open(format=self.format,
                                                channels=self.channels,
                                                rate=self.rate,
                                                input=True,
                                                frames_per_buffer=self.chunk)
        self.stop_event.clear()
        self.audio_thread = threading.Thread(target=self._stream_audio)
        self.audio_thread.start()

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

    def register_callback(self, callback):
        """
        Registers a callback function to process audio data.

        :param callback: Function to process audio data. It should accept a bytes object.
        """
        self.callbacks.append(callback)

    def _stream_audio(self):
        """
        Internal method that reads audio data and calls the registered callbacks.
        """
        while not self.stop_event.is_set():
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            self.frames.append(data)  # Save data for saving to file if needed

            # Put data into queue for processing
            self.audio_queue.put(data)

            # Call all registered callbacks
            for callback in self.callbacks:
                callback(data)

    def save_to_file(self, filename, format='wav'):
        """
        Saves the recorded audio to a file in the specified format.

        :param filename: The filename to save the audio to.
        :param format: The format to save the audio in ('wav' or 'mp3').
        """
        if not self.frames:
            raise ValueError("No audio data to save.")

        audio_data = b''.join(self.frames)

        if format == 'wav':
            wf = wave.open(filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio_interface.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(audio_data)
            wf.close()
        elif format == 'mp3':
            # Use pydub to save to mp3
            from pydub import AudioSegment
            audio_segment = AudioSegment(
                data=audio_data,
                sample_width=self.audio_interface.get_sample_size(self.format),
                frame_rate=self.rate,
                channels=self.channels
            )
            audio_segment.export(filename, format='mp3')
        else:
            raise ValueError("Unsupported format. Use 'wav' or 'mp3'.")

    def get_audio_generator(self):
        """
        Returns a generator that yields audio data chunks.
        """
        while not self.stop_event.is_set():
            try:
                data = self.audio_queue.get(timeout=0.1)
                yield data
            except Empty:
                continue

    def clear_frames(self):
        """
        Clears the stored frames.
        """
        self.frames = []

    def reset(self):
        """
        Resets the streamer by clearing frames and audio queue.
        """
        self.clear_frames()
        while not self.audio_queue.empty():
            self.audio_queue.get()
