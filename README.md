# 🎵 Site de Música

Faculdade: Faesa - Centro Universitário

Disciplina: Programação Back-end

Um site simples feito com Django, HTML e CSS, com o tema musical. Exibe uma página com título, subtítulo, parágrafo, imagem e estilos personalizados.

---

## 🧰 Requisitos

- Python 3.8+
- pip
- (Opcional) Ambiente virtual com `venv`

---

## ⚙️ Como configurar e rodar o projeto

### 1. Clone o repositório ou extraia o ZIP

Se estiver com o projeto zipado:

```bash
unzip site_de_musica.zip
cd site_de_musica
```

### 2. Crie e ative o ambiente virtual (recomendado)

```bash
python -m venv venv
```

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### 3. Atualize o pip

```bash
python -m pip install --upgrade pip
```

### 4. Instale o Django

```bash
pip install django
```

### 5. Rode o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://localhost:8000/musical/
```

---

## 🖼️ Estrutura do Projeto

```
site_de_musica/
├── homepage/
│   ├── static/
│   │   └── homepage/
│   │       ├── styles.css
│   │       ├── sax.jpg
│   │       └── favicon.ico
│   ├── templates/
│   │   └── homepage/
│   │       └── music.html
│   ├── views.py
│   └── ...
├── site_de_musica/
│   ├── settings.py
│   └── ...
└── manage.py
```

---

Desenvolvido para fins educacionais 💻🎶
