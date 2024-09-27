
# YouSound Download

YouSound Download is a Flask-based web application that allows users to download YouTube videos as MP3 or MP4 files. The service is free, without advertising, and respects user privacy by not collecting any data.

## Features

- Download YouTube videos in MP3 or MP4 format.
- User-friendly interface.
- Free to use with no advertisements.
- No data collection or commercial cookies.
- Safe downloads.

## Installation

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/lappatdugain/yousound-download.git
    cd yousound-download
    ```

2. Install dependencies :
    ```bash
    pip install flask
    pip install pytube
    pip install moviepy
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## Usage

1. Open your web browser and go to `http://exemple.com`.
2. Enter the URL of the YouTube video you want to download.
3. Choose the desired format (MP3 or MP4).
4. Click on the "Convert" button to start the download.

## Project Structure

## `ytapp/app.py`

The main entry point of the Flask application. It runs the server and defines the routes.
Contains the Flask views and logic for handling URL submissions and file conversions.

## `templates/index.html`

The HTML template for the main page. It includes:

- A form to submit the YouTube URL and select the conversion type (MP3 or MP4).
- Information about the service in both English and French.
- Navigation menu with links to home, donation page, and Discord.

## `static/`

Contains static files such as CSS, JavaScript, images, and SVG icons used in the web application.

## Logging

The application logs important events and errors to a file named `LogsDownload.log`.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- Discord: [Join our Discord](https://discord.gg/BEJHYj2Z4r)
- Email: [Contact Us](mailto:yousound.xy05v@slmails.com?subject=info%20ytapp)

## Donation

If you find this service useful, consider making a donation:

- [PayPal Donation Link](https://www.paypal.com/donate/?hosted_button_id=ZL6R6GB7QM32G)
