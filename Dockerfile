

FROM TEAMROYAL/Asteroid:1.0.0

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get autoremove --purge

RUN git clone https://github.com/TEAMROYAL/Asteroid.git /root/TEAMROYAL/

WORKDIR /root/TEAMROYAL/

RUN pip3 install -r requirements.txt
RUN npm install -g npm@7.12.1 -g
RUN npm install
RUN npm run build
