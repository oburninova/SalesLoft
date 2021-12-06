FROM python:3.7
WORKDIR /mydir
COPY ./ ./
RUN pip3 install -r requirements.txt
EXPOSE 4000
ENTRYPOINT [ "python3" ]
CMD [ "./app/app.py" ]