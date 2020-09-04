#publicly available docker image "python" on docker hub will be pulled

FROM python:3

#creating directory helloworld in container (linux mach
ADD calculator.py /

ADD test_add.py /

ADD test_multiple.py /

ADD test_divide.py /

ADD test_substract.py /

ADD script.sh /

RUN ["chmod", "+x", "./script.sh"]

CMD ./script.sh
