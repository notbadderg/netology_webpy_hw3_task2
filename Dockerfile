FROM python:3.11.1


COPY ./stocks_products /src/stocks_products

WORKDIR /src/stocks_products

RUN pip install -r requirements.txt

ENV SECRET_KEY="some_key"
ENV DEBUG="True"
ENV ALLOWED_HOSTS="127.0.0.1,localhost"

RUN python manage.py makemigrations
RUN python manage.py migrate


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]