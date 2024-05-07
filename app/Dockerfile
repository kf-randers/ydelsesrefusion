FROM python:3.10-alpine

# Set dir and user
ENV APP_HOME=/app
ENV APP_USER=non-root

# Add user
RUN addgroup $APP_USER && \
    adduser $APP_USER -D -G $APP_USER -h $APP_HOME

# Install packages
#RUN apk update
#RUN apk add postgresql-dev gcc python3-dev musl-dev # Packages needed for psycopg2

# Copy files and set working dir
COPY . $APP_HOME
WORKDIR $APP_HOME

# Install python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Open port
EXPOSE 8080

# Set user
USER $APP_USER

ENTRYPOINT ["python"]
CMD ["app.py"]