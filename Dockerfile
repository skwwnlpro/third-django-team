# 1. 기본 Python 이미지를 지정합니다.
FROM python:3.12-slim

# 2. 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    default-libmysqlclient-dev \
    libmariadb-dev-compat \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 3. pyenv 설치 및 환경 설정
RUN curl https://pyenv.run | bash
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
RUN rm -rf ~/.pyenv/plugins/pyenv-virtualenv && git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
RUN echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# 4. Python 버전 설치 및 가상 환경 생성
RUN /bin/bash -c "source ~/.bashrc && pyenv install 3.12.5"
RUN /bin/bash -c "source ~/.bashrc && pyenv virtualenv 3.12.5 django_app"
RUN echo 'pyenv activate django_app' >> ~/.bashrc

# 5. Poetry 설치
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# 6. 프로젝트 파일 복사 및 의존성 설치
WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock
RUN /bin/bash -c "source ~/.bashrc && pyenv activate django_app && poetry install --no-root"

# 7. 프로젝트 소스 코드 복사
COPY . /app

# 8. ENTRYPOINT 설정
COPY scripts/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/bin/bash", "/app/scripts/entrypoint.sh"]

# 9. Gunicorn이 8000 포트에서 수신하도록 EXPOSE
EXPOSE 8000