# WORDKEEP — English Vocabulary Memory App

## 1. Project Overview

Create a beautiful personal English-learning application designed to help the user **learn new English words and remember them for a long time**.

Main goal:

> Learn a word → understand it → hear it → speak it → review it → remember it.

The application should focus on **English only** for vocabulary content. Do not add Sinhala translations or Sinhala vocabulary.

The app should feel modern, simple, motivating, and enjoyable to use every day.

---

# 2. Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- TypeScript

## Backend

- Python
- Flask

## Database

- SQLite

## Recommended Architecture

```text
English Vocabulary App
│
├── Frontend
│   ├── HTML
│   ├── CSS
│   ├── TypeScript
│   └── JavaScript
│
├── Backend
│   └── Python + Flask
│
├── Database
│   └── SQLite
│
└── Assets
    ├── Icons
    ├── Sounds
    └── Images
```

---

# 3. Main Goal

The application should help the user avoid forgetting words.

For every word, the user should be able to:

- Save the word
- Read the definition
- Read example sentences
- Hear pronunciation
- Practice pronunciation
- Add highlights
- Add words to favorites
- Review words later
- Mark words as difficult
- Track learning progress
- Practice speaking
- Receive daily reminders

---

# 4. English Categories

Every word should have an English category.

## English Type

- 🇺🇸 American English
- 🇬🇧 British English
- Both

The user should be able to filter:

```text
All
American English
British English
```

If pronunciation differs, show both versions.

Example:

```text
Word:
Schedule

American:
 /ˈskedʒuːl/

British:
 /ˈʃedjuːl/
```

---

# 5. Add New Word

Create a large **+ Add Word** button.

The Add Word screen should contain:

## Word

Example:

```text
Improve
```

## Word Type

Dropdown:

```text
Noun
Verb
Adjective
Adverb
Pronoun
Preposition
Conjunction
Interjection
Phrase
Idiom
Other
```

## English Type

```text
American English
British English
Both
```

## Definition

Example:

```text
To make something better.
```

## Example Sentence

Example:

```text
I want to improve my English.
```

## Second Example

Optional:

```text
She improved her speaking skills.
```

## Personal Note

Example:

```text
Important word for speaking practice.
```

## Difficulty

```text
Easy
Medium
Hard
Very Hard
```

## Save

```text
SAVE WORD
```

---

# 6. Word Detail Page

When the user opens a word, show a beautiful vocabulary card.

Example:

```text
━━━━━━━━━━━━━━━━━━━━━━

        IMPROVE

        Verb

🇺🇸 American English

To make something better.

🔊 Pronunciation

/imˈpruːv/

━━━━━━━━━━━━━━━━━━━━━━

Example

“I want to improve my English.”

━━━━━━━━━━━━━━━━━━━━━━

[ 🔊 Speak ]

[ ⭐ Favorite ]

[ 🖍 Highlight ]

[ 🔁 Practice ]

━━━━━━━━━━━━━━━━━━━━━━
```

---

# 7. Speak Button

Every word must have a **Speak** button.

```text
🔊 Speak
```

When clicked, the application should pronounce the word.

Use browser Speech Synthesis or another TTS service.

The user should be able to choose:

```text
🇺🇸 American Voice
🇬🇧 British Voice
```

Flow:

```text
User clicks Speak
       ↓
JavaScript / TypeScript
       ↓
Speech Engine
       ↓
English pronunciation
```

---

# 8. Speaking Practice

Create a dedicated:

# Speaking Practice

The purpose is to help the user actually say the words.

Example:

```text
              SPEAKING PRACTICE

                  IMPROVE

       “I want to improve my English.”

                  🔊 Listen

                    ↓

              🎤 Your Turn

          [ Start Speaking ]

                    ↓

            Speech recognition

                    ↓

       Pronunciation feedback
```

Possible result:

```text
Great!

Word:
Improve

Your pronunciation:
Good

Accuracy:
86%

[ Try Again ]
```

Use browser Speech Recognition where available.

---

# 9. Highlight Button

Add a highlight feature.

Button:

```text
🖍 Highlight
```

Possible highlight levels:

```text
Normal
Important
Very Important
Must Remember
```

Highlighted words should appear differently in the vocabulary list.

Example:

```text
⭐ Important Word

Improve
```

The user can remove the highlight later.

---

# 10. Star / Favorite System

Every word should have:

```text
☆ Favorite
```

After clicking:

```text
★ Favorite
```

Create a Favorites page containing all starred words.

Example:

```text
★ Improve
★ Confidence
★ Opportunity
★ Experience
★ Comfortable
```

---

# 11. Difficulty and Memory Status

Each vocabulary word should have a memory status:

```text
New
Learning
Remembering
Strong
Forgotten
```

Example:

```text
Improve

Status:
Learning

Memory:
65%
```

---

# 12. Daily Reminder

Create a dedicated:

# Daily Words

The app should remind the user every day.

Example:

```text
☀️ GOOD MORNING

Today's English Words

1. Improve
2. Opportunity
3. Comfortable
4. Experience
5. Confident

You have 5 words to review.

[ START REVIEW ]
```

The reminder should encourage the user without becoming annoying.

---

# 13. “Don't Forget These Words”

This is one of the main features.

Create:

# 🧠 Don't Forget

The app automatically puts difficult or frequently forgotten words here.

Example:

```text
DON'T FORGET

⚠ Comfortable
⚠ Necessary
⚠ Opportunity
⚠ Environment

You struggled with these words recently.

[ REVIEW NOW ]
```

A word becomes more important when the user repeatedly gets it wrong.

---

# 14. Smart Review System

Use a simple spaced-review system.

Each word should contain:

```text
created_at
last_reviewed
next_review
review_count
correct_count
wrong_count
memory_score
```

Example review schedule:

```text
New Word
   ↓
10 minutes
   ↓
1 day
   ↓
3 days
   ↓
7 days
   ↓
14 days
   ↓
30 days
   ↓
60 days
```

If the user forgets a word:

```text
Forgot
 ↓
Move closer review
 ↓
Review again
```

If the user remembers it:

```text
Correct
 ↓
Increase memory score
 ↓
Longer review interval
```

---

# 15. Review Screen

Create a focused review screen.

Example:

```text
        DAILY REVIEW

             7 / 10

          OPPORTUNITY

        What does it mean?

      [ Show Answer ]
```

After showing:

```text
Opportunity

A favorable time or chance
for something to happen.

Example:

“This is a great opportunity.”

Did you remember it?

[ 😕 Forgot ]

[ 😐 Hard ]

[ 🙂 Good ]

[ 😎 Easy ]
```

The result should affect the next review date.

---

# 16. Quiz Mode

Add vocabulary quizzes.

## Multiple Choice

```text
What does “Improve” mean?

○ To make something better
○ To leave somewhere
○ To become angry
○ To forget something
```

## Fill in the Blank

```text
I want to ______ my English.

[ improve ]
```

## Word Meaning

```text
Definition:
“To make something better.”

What is the word?

[ Improve ]
```

## Listening Quiz

```text
🔊 Listen

Which word did you hear?

○ Improve
○ Approve
○ Remove
○ Prove
```

---

# 17. Search

Create:

```text
🔍 Search English words...
```

Search by:

- Word
- Definition
- Example
- Category
- Difficulty
- Favorite
- Highlight
- Memory status

Filters:

```text
All Words
Favorites
Highlighted
Difficult
Forgotten
Learning
Strong
American English
British English
```

---

# 18. Dashboard

Create a beautiful main dashboard.

Example:

```text
╭─────────────────────────────────╮
│       MY ENGLISH JOURNEY         │
│                                 │
│        247 Words Learned        │
│                                 │
│     🔥 14 Day Learning Streak  │
╰─────────────────────────────────╯


TODAY

📖 New Words              5

🧠 Review Words           8

🎤 Speaking Practice      3

⭐ Favorite Words         27


─────────────────────────────────

Memory Progress

██████████████░░░ 82%


─────────────────────────────────

DON'T FORGET

⚠ Opportunity
⚠ Comfortable
⚠ Necessary


[ START DAILY REVIEW ]
```

---

# 19. Statistics

Create a Statistics page.

Show:

```text
Total Words
247

Strong Words
142

Learning
67

Difficult
38

Favorites
27

Speaking Practices
184

🔥 Current Streak
14 Days

🏆 Best Streak
21 Days
```

---

# 20. Progress Charts

Display:

- Words learned
- Words reviewed
- Speaking practices
- Memory score
- Daily streak

Time filters:

```text
1 Week
1 Month
3 Months
6 Months
1 Year
```

---

# 21. Calendar

Create a learning calendar.

Example:

```text
September 2026

Mon Tue Wed Thu Fri Sat Sun
                         1
 2   3   4   5   6   7   8
 9  10  11  12  13  14  15
```

Days where the user practiced should be visually marked.

---

# 22. Learning Streak

Create:

```text
🔥 14 DAY STREAK
```

Show:

```text
Current Streak
Best Streak
Words This Week
Practice Minutes
```

The goal is consistency rather than pressure.

---

# 23. Categories

Default categories:

```text
General English
Daily Conversation
Work
Technology
Travel
Education
Business
Gaming
Movies & TV
Social Life
Speaking
Academic
Useful Phrases
Idioms
```

Allow the user to create custom categories.

---

# 24. Phrase / Sentence Learning

Do not limit the app to individual words.

Allow:

```text
Words
Phrases
Expressions
Idioms
Sentences
```

Example:

```text
“I’m looking forward to it.”

Type:
Phrase

Meaning:
Used when you are excited about something
that will happen in the future.
```

---

# 25. Word Relationships

Add related vocabulary.

Example:

```text
Improve

Synonyms:
Develop
Enhance
Upgrade

Related:
Improvement
Improved
Improving
```

---

# 26. Personal Notes

Allow the user to add personal notes.

Example:

```text
Why I want to remember this:

Useful for workplace conversations.
```

This makes words personally meaningful.

---

# 27. Word History

Each word should have a history.

Example:

```text
WORD HISTORY

Added:
September 11, 2026

Reviewed:
September 11, 2026

Times reviewed:
8

Correct:
6

Forgot:
2

Memory score:
78%
```

---

# 28. UI Theme

Create a premium modern learning-app design.

Design style:

- Clean
- Minimal
- Modern
- Soft rounded cards
- Smooth animations
- Large readable typography
- Good spacing
- Dark mode
- Light mode
- Responsive layout

The app should feel like a premium productivity/learning application.

---

# 29. Light Mode

```text
Background:
Very light neutral

Cards:
White

Text:
Dark charcoal

Accent:
Modern blue/purple
```

---

# 30. Dark Mode

```text
Background:
Dark charcoal

Cards:
Dark gray

Text:
White

Accent:
Blue/purple
```

Add:

```text
☀ Light
🌙 Dark
```

Save the selected theme in local storage.

---

# 31. Mobile First

The application should work extremely well on phones.

Mobile navigation:

```text
┌───────────────────────┐
│ English Memory        │
│                       │
│ Today                 │
│                       │
│ + Add Word            │
│                       │
│ 🧠 Review             │
│ 🎤 Speaking           │
│ ⭐ Favorites          │
│                       │
│ Don't Forget          │
│                       │
└───────────────────────┘

 Home   Words   Review   Stats
```

Desktop should use a sidebar.

---

# 32. Navigation

Main navigation:

```text
🏠 Dashboard

📖 My Words

➕ Add Word

🧠 Review

🎤 Speaking

⭐ Favorites

🖍 Highlights

⚠ Don't Forget

📝 Quiz

📊 Statistics

📅 Calendar

⚙ Settings
```

---

# 33. Settings

Include:

## Pronunciation

```text
🇺🇸 American
🇬🇧 British
```

## Daily Goal

```text
5 words
10 words
15 words
20 words
Custom
```

## Daily Reminder

```text
ON / OFF
```

## Reminder Time

```text
08:00 AM
```

## Dark Mode

```text
ON / OFF
```

## Sound

```text
ON / OFF
```

---

# 34. Notifications

Possible notifications:

```text
🧠 Time for your English review.

You have 7 words waiting.
```

```text
🔥 Keep your streak alive!

Practice a few English words today.
```

```text
⚠ You have 4 difficult words to review.
```

Notifications should be useful and not excessive.

---

# 35. Motivation System

Use small motivational messages:

```text
Keep going. One word at a time.

You remembered this word!

Nice pronunciation.

Your vocabulary is growing.

You haven’t reviewed this word recently.

Great work today!
```

Do not make the app feel like school homework.

---

# 36. Database Design

Use SQLite.

## users

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## categories

```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

## words

```sql
CREATE TABLE words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    word_type TEXT,
    english_type TEXT,
    definition TEXT NOT NULL,
    example_sentence TEXT,
    second_example TEXT,
    personal_note TEXT,
    difficulty TEXT,
    category_id INTEGER,
    pronunciation_us TEXT,
    pronunciation_uk TEXT,
    favorite INTEGER DEFAULT 0,
    highlighted INTEGER DEFAULT 0,
    highlight_level TEXT DEFAULT 'Normal',
    memory_status TEXT DEFAULT 'New',
    memory_score INTEGER DEFAULT 0,
    review_count INTEGER DEFAULT 0,
    correct_count INTEGER DEFAULT 0,
    wrong_count INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_reviewed DATETIME,
    next_review DATETIME,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

## reviews

```sql
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    result TEXT NOT NULL,
    reviewed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (word_id) REFERENCES words(id)
);
```

## speaking_practice

```sql
CREATE TABLE speaking_practice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER,
    score INTEGER,
    practiced_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (word_id) REFERENCES words(id)
);
```

## learning_days

```sql
CREATE TABLE learning_days (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT UNIQUE,
    words_learned INTEGER DEFAULT 0,
    reviews_completed INTEGER DEFAULT 0,
    speaking_sessions INTEGER DEFAULT 0
);
```

---

# 37. Flask REST API

Create:

```text
GET    /api/words
GET    /api/words/<id>
POST   /api/words
PUT    /api/words/<id>
DELETE /api/words/<id>

GET    /api/review
POST   /api/review/<id>

GET    /api/favorites
POST   /api/words/<id>/favorite

POST   /api/words/<id>/highlight

GET    /api/statistics
GET    /api/streak
GET    /api/calendar

GET    /api/categories
POST   /api/categories
```

---

# 38. Search API

Example:

```text
GET /api/words?search=improve
```

Filters:

```text
/api/words?favorite=true
/api/words?highlighted=true
/api/words?status=Forgotten
/api/words?english_type=American
```

---

# 39. Security

Use good development practices:

- Validate all input
- Sanitize text where appropriate
- Use parameterized SQL queries
- Never concatenate SQL strings with user input
- Store configuration in environment variables
- Use `.env` for secrets
- Do not commit API keys
- Add `.gitignore`
- Protect Flask secret keys

Example `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
instance/
*.db
```

---

# 40. Professional Project Structure

```text
english-memory-app/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── models/
│   │   └── word.py
│   │
│   ├── routes/
│   │   ├── words.py
│   │   ├── review.py
│   │   ├── statistics.py
│   │   └── speaking.py
│   │
│   ├── services/
│   │   ├── review_engine.py
│   │   ├── pronunciation.py
│   │   └── statistics.py
│   │
│   └── db/
│       └── vocabulary.db
│
├── frontend/
│   ├── index.html
│   │
│   ├── pages/
│   │   ├── dashboard.html
│   │   ├── words.html
│   │   ├── add-word.html
│   │   ├── review.html
│   │   ├── speaking.html
│   │   ├── favorites.html
│   │   └── statistics.html
│   │
│   ├── css/
│   │   ├── main.css
│   │   ├── responsive.css
│   │   └── themes.css
│   │
│   └── ts/
│       ├── app.ts
│       ├── words.ts
│       ├── review.ts
│       ├── speaking.ts
│       ├── dashboard.ts
│       └── settings.ts
│
├── static/
│   ├── icons/
│   └── audio/
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── package.json
├── tsconfig.json
├── README.md
└── LICENSE
```

---

# 41. Import and Export

Add CSV import.

Example:

```text
word,definition,example,category,english_type
improve,make something better,I want to improve my English,Speaking,American
```

Features:

- Import vocabulary from CSV
- Export vocabulary to CSV
- Download database backup
- Restore database backup

---

# 42. Word of the Day

Show one useful word every day.

```text
WORD OF THE DAY

CONFIDENT

Feeling sure about your abilities.

Example:
“She feels confident when speaking English.”

[ Practice ]
```

---

# 43. Random Word

Add:

```text
🎲 Random Word
```

This randomly selects a saved vocabulary item.

---

# 44. Main User Flow

## First Time

```text
Open App
 ↓
Welcome Screen
 ↓
Set Daily Goal
 ↓
Choose American / British English
 ↓
Dashboard
```

## Add Word

```text
Add Word
 ↓
Enter Word
 ↓
Definition
 ↓
Example
 ↓
English Type
 ↓
Difficulty
 ↓
Save
```

## Learn

```text
Open Word
 ↓
Read
 ↓
Listen
 ↓
Speak
 ↓
Practice
 ↓
Mark difficulty
```

## Review

```text
Daily Reminder
 ↓
Review
 ↓
Answer
 ↓
Forgot / Hard / Good / Easy
 ↓
Update Memory Score
 ↓
Set Next Review
```

---

# 45. MVP Version

Build the first version with:

1. Dashboard
2. Add English words
3. SQLite database
4. Word list
5. Search
6. American/British English
7. Speak button
8. Favorite/star
9. Highlight
10. Daily review
11. Don't Forget section
12. Basic spaced repetition
13. Speaking practice
14. Statistics
15. Dark/light theme
16. Responsive mobile UI

Build these first before advanced features.

---

# 46. Future Version

Later add:

- AI-generated example sentences
- AI word explanations
- AI conversation practice
- AI speaking feedback
- Automatic synonym generation
- Automatic word difficulty
- Voice conversation
- Listening exercises
- Grammar practice
- Sentence-building exercises
- Progress achievements
- Cloud synchronization
- Android application
- Desktop application

---

# 47. App Identity

Recommended name:

# WORDKEEP

Tagline:

> Learn words. Keep them. Use them.

Alternative names:

- WORDMIND
- VOCABLOOM
- MEMOENGLISH
- LEXIMIND

---

# 48. Learning Philosophy

The application should prioritize **active recall and repeated exposure**.

The main learning cycle:

```text
READ
 ↓
LISTEN
 ↓
SPEAK
 ↓
RECALL
 ↓
USE
 ↓
REVIEW
 ↓
REMEMBER
```

The application should not simply be a dictionary.

It should act as a **personal English memory trainer**.

---

# 49. Final Product Vision

The finished application should feel like a combination of:

```text
Vocabulary Notebook
        +
Spaced Repetition
        +
Speaking Practice
        +
Daily Habit Tracker
        +
Personal Dictionary
```

The central concept is:

> **“I learned this word, and I don't want to forget it.”**

Every feature should support that goal.
