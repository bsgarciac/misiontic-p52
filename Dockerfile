FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /users
WORKDIR /users
ADD . /users/
# ESTO ES UN COMENTARIO 
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT