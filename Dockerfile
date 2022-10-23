FROM python:3.10

WORKDIR /home/denis/projects/blogfastapi/BlogFastAPI

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python3", "src/app/main.py"]