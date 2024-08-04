# requirements.txt

```txt
Django==4.2.3
djangorestframework==3.14.0
django-cors-headers==4.1.0

```

# manage.py

```py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'age_fit_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```

# db.sqlite3

This is a binary file of the type: Binary

# .gitignore

```
# Python
__pycache__/
*.py[cod]
*.so

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Vue
node_modules/
/dist/

# Environment
.env
.venv
env/
venv/
ENV/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Vue.js
/frontend/node_modules
/frontend/dist
```

# frontend\vue.config.js

```js
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

```

# frontend\tailwind.config.js

```js
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}

```

# frontend\README.md

```md
# frontend

## Project setup
\`\`\`
npm install
\`\`\`

### Compiles and hot-reloads for development
\`\`\`
npm run serve
\`\`\`

### Compiles and minifies for production
\`\`\`
npm run build
\`\`\`

### Lints and fixes files
\`\`\`
npm run lint
\`\`\`

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

```

# frontend\postcss.config.js

```js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}

```

# frontend\package.json

```json
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint"
  },
  "dependencies": {
    "core-js": "^3.8.3",
    "vue": "^3.2.13"
  },
  "devDependencies": {
    "@babel/core": "^7.12.16",
    "@babel/eslint-parser": "^7.12.16",
    "@vue/cli-plugin-babel": "~5.0.0",
    "@vue/cli-plugin-eslint": "~5.0.0",
    "@vue/cli-service": "~5.0.0",
    "autoprefixer": "^10.4.20",
    "eslint": "^7.32.0",
    "eslint-plugin-vue": "^8.0.3",
    "postcss": "^8.4.40",
    "tailwindcss": "^3.4.7"
  },
  "eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/vue3-essential",
      "eslint:recommended"
    ],
    "parserOptions": {
      "parser": "@babel/eslint-parser"
    },
    "rules": {}
  },
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead",
    "not ie 11"
  ]
}

```

# frontend\jsconfig.json

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "esnext",
    "baseUrl": "./",
    "moduleResolution": "node",
    "paths": {
      "@/*": [
        "src/*"
      ]
    },
    "lib": [
      "esnext",
      "dom",
      "dom.iterable",
      "scripthost"
    ]
  }
}

```

# frontend\babel.config.js

```js
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ]
}

```

# frontend\.gitignore

```
.DS_Store
node_modules
/dist


# local env files
.env.local
.env.*.local

# Log files
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# Editor directories and files
.idea
.vscode
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

```

# core\__init__.py

```py

```

# core\views.py

```py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import CustomUser, Exercise, Program, WorkoutDay, ProgramExercise, Workout, WorkoutExercise, BodyWeightLog
from .serializers import CustomUserSerializer, ExerciseSerializer, ProgramSerializer, WorkoutDaySerializer, ProgramExerciseSerializer, WorkoutSerializer, WorkoutExerciseSerializer, BodyWeightLogSerializer

def home(request):
    return HttpResponse("<h1>Welcome to Age Fit App</h1>")

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class WorkoutDayViewSet(viewsets.ModelViewSet):
    queryset = WorkoutDay.objects.all()
    serializer_class = WorkoutDaySerializer

class ProgramExerciseViewSet(viewsets.ModelViewSet):
    queryset = ProgramExercise.objects.all()
    serializer_class = ProgramExerciseSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer

class BodyWeightLogViewSet(viewsets.ModelViewSet):
    queryset = BodyWeightLog.objects.all()
    serializer_class = BodyWeightLogSerializer
```

# core\urls.py

```py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home,  # Add this import
    CustomUserViewSet,
    ExerciseViewSet,
    ProgramViewSet,
    WorkoutDayViewSet,
    ProgramExerciseViewSet,
    WorkoutViewSet,
    WorkoutExerciseViewSet,
    BodyWeightLogViewSet
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'workout-days', WorkoutDayViewSet)
router.register(r'program-exercises', ProgramExerciseViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'workout-exercises', WorkoutExerciseViewSet)
router.register(r'body-weight-logs', BodyWeightLogViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
```

# core\tests.py

```py
from django.test import TestCase

# Create your tests here.

```

# core\serializers.py

```py
from rest_framework import serializers
from .models import CustomUser, Exercise, Program, WorkoutDay, ProgramExercise, Workout, WorkoutExercise, BodyWeightLog

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'date_of_birth', 'height', 'fitness_level')
        extra_kwargs = {'password': {'write_only': True}}

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class WorkoutDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutDay
        fields = '__all__'

class ProgramExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramExercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = '__all__'

class BodyWeightLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyWeightLog
        fields = '__all__'

```

# core\models.py

```py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)  # in cm
    fitness_level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ], default='beginner')

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(blank=True)

class Program(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WorkoutDay(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    day_number = models.IntegerField()

class ProgramExercise(models.Model):
    workout_day = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    target_weight = models.FloatField()

class Workout(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    is_completed = models.BooleanField(default=False)
    is_partial = models.BooleanField(default=False)
    comments = models.TextField(blank=True)

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    planned_sets = models.IntegerField()
    planned_reps = models.IntegerField()
    planned_weight = models.FloatField()
    actual_sets = models.IntegerField(null=True, blank=True)
    actual_reps = models.IntegerField(null=True, blank=True)
    actual_weight = models.FloatField(null=True, blank=True)
    is_skipped = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

class BodyWeightLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()

```

# core\apps.py

```py
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

```

# core\admin.py

```py
from django.contrib import admin

# Register your models here.

```

# age_fit_project\__init__.py

```py

```

# age_fit_project\wsgi.py

```py
"""
WSGI config for age_fit_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'age_fit_project.settings')

application = get_wsgi_application()
```

# age_fit_project\urls.py

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

```

# age_fit_project\settings.py

```py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key-here'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'core',  # Move this to the top
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'age_fit_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'age_fit_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True  # For development only, configure properly for production

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

AUTH_USER_MODEL = 'core.CustomUser'
   

```

# age_fit_project\asgi.py

```py
"""
ASGI config for age_fit_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'age_fit_project.settings')

application = get_asgi_application()

```

# frontend\src\main.js

```js
import './assets/tailwind.css'
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

```

# frontend\src\App.vue

```vue
<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

# frontend\public\index.html

```html
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title><%= htmlWebpackPlugin.options.title %></title>
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </body>
</html>

```

# frontend\public\favicon.ico

This is a binary file of the type: Binary

# core\migrations\__init__.py

```py

```

# core\migrations\0001_initial.py

```py
# Generated by Django 4.2.3 on 2024-08-04 20:22

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('fitness_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('video_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_completed', models.BooleanField(default=False)),
                ('is_partial', models.BooleanField(default=False)),
                ('comments', models.TextField(blank=True)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_sets', models.IntegerField()),
                ('planned_reps', models.IntegerField()),
                ('planned_weight', models.FloatField()),
                ('actual_sets', models.IntegerField(blank=True, null=True)),
                ('actual_reps', models.IntegerField(blank=True, null=True)),
                ('actual_weight', models.FloatField(blank=True, null=True)),
                ('is_skipped', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.workout')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('target_weight', models.FloatField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.exercise')),
                ('workout_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.workoutday')),
            ],
        ),
        migrations.CreateModel(
            name='BodyWeightLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weight', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

```

# frontend\src\components\HelloWorld.vue

```vue
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
      <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a></li>
      <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

```

# frontend\src\assets\tailwind.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

```

# frontend\src\assets\logo.png

This is a binary file of the type: Image

