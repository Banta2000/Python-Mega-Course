import time
import cv2
from emailing import send_email
import streamlit as st
import glob
import os


def clean_folder():
    images = glob.glob("images/*.jpg")
    for image in images:
        os.remove(image)


st.title("Webcam Live Feed")
start = st.button("Start Camera")


if start:
    streamlit_image = st.image([])
    video = cv2.VideoCapture(0)
    time.sleep(1)

    first_frame = None
    status_list = []

    count = 1

    while True:
        check, frame = video.read()
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        status = 0

        # Draw a white box in the top left corner
        cv2.rectangle(frame, (5, 5), (150, 60), (255, 255, 255), -1)

        # Add Date and Time to the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, time.strftime("%d.%m.%y"), (10, 30), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, time.strftime("%H:%M:%S"), (10, 50), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

        # Create first frame
        if first_frame is None:
            first_frame = gray_frame_gau
            continue

        # Diff Frame, apply threhold
        delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
        thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
        dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

        contours, check = cv2.findContours(dil_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            if rectangle.any():
                status = 1
                cv2.imwrite(f"images/{count}.jpg", frame)
                count += 1
                all_images = glob.glob("images/*.jpg")
                index = int(len(all_images) / 2)
                image_with_object = all_images[index]

        # Status List = Last two status. 1 : Object detected, 0 : No object detected
        status_list.append(status)
        status_list = status_list[-2:]

        # Check if object left the screen, if so send email
        if status_list[0] == 1 and status_list[1] == 0:
            send_email(image_with_object)
            clean_folder()

        # cv2.imshow("Captured Frame", frame)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        streamlit_image.image(rgb_frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    video.release()
