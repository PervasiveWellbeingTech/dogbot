FROM python:3.6

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

ENV PATH /opt/conda/bin:$PATH

COPY environment.yml
COPY sfx
COPY DogBot.py
COPY main.py
COPY settings.py

RUN conda env create -f environment.yml
RUN conda create --name myenv python=3.6
RUN /bin/bash -c ". activate dogbot_p36"

CMD [ "python", "./main.py" ]
