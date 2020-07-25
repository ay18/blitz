FROM python
WORKDIR /blitz
COPY . .
RUN pip install -r requirements.txt
RUN python main.py