# Django Blog Website Development — Completed Tasks

## 1. Frontend Design
- প্রথমে Tailwind CSS ব্যবহার করে HTML ফাইলে Blog Website-এর ডিজাইন তৈরি করেছি।
- ওয়েবসাইটে কী ধরনের layout, category section এবং blog post card থাকবে, তা নির্ধারণ করেছি।

## 2. Project Setup
- কম্পিউটারে প্রজেক্টের জন্য একটি folder তৈরি করেছি।
- GitHub-এ একটি repository তৈরি করে local project folder-এর সঙ্গে connect করেছি।
- Virtual environment setup করেছি এবং Django install করেছি।
- Django project তৈরি করেছি এবং এর মধ্যে একটি app তৈরি করেছি।

## 3. Django Configuration
- Project-এর `settings.py` ফাইলে template directory configure করেছি।
- App-টিকে `INSTALLED_APPS`-এ যুক্ত করেছি।
- App-এর URL configuration-কে main project-এর `urls.py`-এর সঙ্গে connect করেছি।
- App-এর মধ্যে static folder তৈরি করে static files ব্যবহারের জন্য প্রয়োজনীয় configuration করেছি।

## 4. Database Model and Migration
- Category-এর জন্য একটি model তৈরি করেছি।
- Model অনুযায়ী database migration তৈরি করেছি এবং database-এ migration apply করেছি।
- Django Admin Panel-এ Category model register করেছি।
- Admin Panel ব্যবহার করে database-এ কয়েকটি category তৈরি করেছি।

## 5. Views and Category Display
- Category model থেকে data retrieve করার জন্য `views.py`-তে function তৈরি করেছি।
- প্রয়োজনীয় model objects retrieve করে context dictionary-তে রেখেছি।
- `render()` function ব্যবহার করে data HTML template-এ পাঠিয়েছি।
- Django template-এর logic ব্যবহার করে category-গুলো ওয়েবসাইটে dynamically display করেছি।

## 6. BlogPost Model Development

`BlogPost` নামে একটি Django model তৈরি করেছি, যেখানে blog post-এর প্রয়োজনীয় তথ্য সংরক্ষণের জন্য নিচের field-গুলো নির্ধারণ করেছি।

| Field | কাজ |
|---|---|
| `title` | Blog post-এর title সংরক্ষণ করে |
| `slug` | Blog post-এর জন্য unique slug সংরক্ষণ করে |
| `category` | `Category` model-এর সঙ্গে ForeignKey relationship তৈরি করে |
| `author` | Django-এর `User` model-এর সঙ্গে ForeignKey relationship তৈরি করে |
| `short_description` | Blog-এর সংক্ষিপ্ত বিবরণ সংরক্ষণ করে |
| `blog_body` | Blog-এর মূল লেখা সংরক্ষণ করে |
| `status` | `STATUS_MODE` choices ব্যবহার করে post-এর status নির্ধারণ করে |
| `is_feature` | Blog post-টি featured কি না, তা Boolean value দিয়ে নির্ধারণ করে |
| `created_at` | Post তৈরির সময় সংরক্ষণের জন্য ব্যবহার করেছি |
| `updated_at` | Post update হওয়ার সময় সংরক্ষণের জন্য ব্যবহার করেছি |

### Model-এর গুরুত্বপূর্ণ বিষয়গুলো

- `ForeignKey` ব্যবহার করে `BlogPost` model-এর সঙ্গে `Category` ও `User` model-এর relationship তৈরি করেছি।
- `on_delete=models.CASCADE` ব্যবহার করেছি, যাতে সংশ্লিষ্ট Category বা User delete হলে তার সঙ্গে সম্পর্কিত BlogPost-গুলোও delete হয়।
- `slug` field-এ `unique=True` ব্যবহার করেছি, যাতে একই slug একাধিক post-এ ব্যবহার না করা যায়।
- `choices=STATUS_MODE` ব্যবহার করে post-এর status নির্দিষ্ট কিছু option-এর মধ্যে সীমাবদ্ধ করেছি।
- `default=False` ব্যবহার করে নতুন post-কে default হিসেবে featured না রাখার ব্যবস্থা করেছি।
- `auto_now=True` ব্যবহার করেছি `created_at` ও `updated_at` field-এর সময় স্বয়ংক্রিয়ভাবে update করার জন্য।

এরপর `BlogPost` model-টি Django Admin Panel-এ register করেছি এবং Admin Panel থেকে blog post তৈরি করেছি। পরে `views.py`-তে প্রয়োজনীয় data retrieve করে context dictionary-এর মাধ্যমে HTML template-এ পাঠিয়েছি এবং Django Template Language ব্যবহার করে blog post-গুলো dynamically display করেছি।

## 7. Blog Post Data Integration
- `views.py`-তে function তৈরি করে `BlogPost` model থেকে প্রয়োজনীয় data retrieve করেছি।
- Context dictionary-এর মাধ্যমে retrieved data HTML template-এ পাঠিয়েছি।
- HTML template-এ Django Template Language ব্যবহার করে blog post-এর title, short description এবং প্রয়োজনীয় তথ্য dynamically display করেছি।
- Frontend-এর blog card-এর সঙ্গে backend-এর database data connect করেছি।

## 8. Server Testing
- Django development server চালু করেছি।
- Browser-এ ওয়েবসাইট open করে category এবং blog post-এর data সঠিকভাবে display হচ্ছে কি না পরীক্ষা করেছি।

## Summary
এ পর্যন্ত আমি একটি Django Blog Website-এর basic setup, frontend integration, database model creation, admin panel configuration, views, URL routing, static files configuration এবং dynamic data rendering-এর কাজ সম্পন্ন করেছি। Frontend-এর HTML template-এর সঙ্গে Django backend ও database-এর সংযোগ স্থাপন করেছি।
