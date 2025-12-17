FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    perl \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-pictures \
    lmodern \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir latex babanovtex_external
RUN mkdir -p /usr/local/share/texmf/tex/latex
ENV PATH="/usr/local/texlive/bin/x86_64-linux:${PATH}"
WORKDIR /workspace

CMD ["bash"]