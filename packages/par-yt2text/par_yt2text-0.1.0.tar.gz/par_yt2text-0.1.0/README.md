# PAR YT2Text

[![PyPI](https://img.shields.io/pypi/v/par_yt2text)](https://pypi.org/project/par_yt2text/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/par_yt2text.svg)](https://pypi.org/project/par_yt2text/)  
![Runs on Linux | MacOS | Windows](https://img.shields.io/badge/runs%20on-Linux%20%7C%20MacOS%20%7C%20Windows-blue)
![Arch x86-63 | ARM | AppleSilicon](https://img.shields.io/badge/arch-x86--64%20%7C%20ARM%20%7C%20AppleSilicon-blue)  
![PyPI - License](https://img.shields.io/pypi/l/par_yt2text)

PAR YT2Text Based on yt By Daniel Miessler with the addition of OpenAI Whisper for videos that don't have transcripts.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/probello3)


## Features

- Extract metadata, transcripts, and comments from YouTube videos
- If the transcript is not available, optionally use OpenAI Whisper API to transcribe the audio


## Prerequisites

* To install PAR YT2Text, make sure you have Python 3.11.
* Create a GOOGLE API key
* If you want to use OpenAI Whisper API, create an OPENAI API key

### [uv](https://pypi.org/project/uv/) is recommended

#### Linux and Mac
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Installation

### Installation From Source

Then, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/paulrobello/par_yt2text.git
   cd par_yt2text
   ```

2. Install the package dependencies using uv:
   ```bash
   uv sync
   ```

### Installation From PyPI

To install PAR YT2Text from PyPI, run any of the following commands:

```bash
uv tool install par_yt2text
```

```bash
pipx install par_yt2text
```

## Usage
Create a file called `~/.par_yt2text.env` with your Google API key and OpenAI API key in it.
```bash
GOOGLE_API_KEY= # needed for youtube-transcript-api
OPENAI_API_KEY= # needed for OpenAI whisper audio transcription
PAR_YT2TEXT_SAVE_DIR= # where to save the transcripts if you dont specify a folder in the --save option
```
Whisper audio transcription will only be used if you specify the `--whisper` option and the video does not have a transcript.

Often the transcript will come back a single long line. 
PAR YT2Text will attempt to add newlines to the transcript to make it easier to read unless you specify the `--no-fix-newlines` option.


### Running from source
```bash
uv run par_yt2text --transcript --whisper 'https://www.youtube.com/watch?v=COSpqsDjiiw'
```

### Running if installed from PyPI
```bash
par_yt2text --transcript --whisper 'https://www.youtube.com/watch?v=COSpqsDjiiw'
```

### Options
```
usage: par_yt2text [-h] [--duration] [--transcript] [--comments] [--metadata] [--no-fix-newlines] [--whisper]
                   [--whisper-model WHISPER_MODEL] [--lang LANG] [--save FILE]
                   url

positional arguments:
  url                   YouTube video URL

options:
  -h, --help            show this help message and exit
  --duration            Output only the duration
  --transcript          Output only the transcript
  --comments            Output the comments on the video
  --metadata            Output the video metadata
  --no-fix-newlines     Dont attempt to fix missing newlines from sentences
  --whisper             Use OpenAI Whisper to transcribe the audio if transcript is not available
  --whisper-model WHISPER_MODEL
                        Whisper model to use for audio transcription (default: whisper-1)
  --lang LANG           Language for the transcript (default: English)
  --save FILE           Save the output to a file
```


## Whats New
- Version 0.1.0:
  - Initial release

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Paul Robello - probello@gmail.com  (Based on yt By Daniel Miessler)
