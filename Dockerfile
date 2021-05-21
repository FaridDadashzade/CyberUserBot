FROM siriuserbot/siriuserbot:latest
RUN git clone https://github.com/FaridDadashzade/CyberUserBot /root/CyberUserBot
WORKDIR /root/CyberUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
