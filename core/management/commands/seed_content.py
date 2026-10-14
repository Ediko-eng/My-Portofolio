from django.core.management.base import BaseCommand

from core.models import Profile, Project, Skill

PROFILE = {
    "name": "Edmilson Fabio Valente",
    "logo_text": "E.V.Dev",
    "job_title": "Web Developer & ML/AI Enthusiast",
    "subtitle": "Informatics Engineering student · Web developer · ML/AI enthusiast",
    "about": (
        "Hello! I'm Edmilson Fabio Valente, a dedicated student at UNTL's Faculty of "
        "Engineering, Science, and Technology, majoring in Informatics Engineering. I'm a "
        "developer driven by a passion for building intelligent, elegant solutions that "
        "solve real-world problems.\n\n"
        "Currently, I specialize in Web Development and am deeply immersed in Machine "
        "Learning and Deep Learning. I believe the future lies at the intersection of "
        "beautiful interfaces and powerful data-driven insights. My primary tool is Python, "
        "and I constantly push boundaries.\n\n"
        "I'm on a focused journey to master AI while refining my software engineering craft. "
        "Coding isn't just about writing scripts—it's the continuous pursuit of knowledge "
        "and delivering high-quality, innovative results."
    ),
    "university": "UNTL · Informatics Engineering",
    "email": "edmilsonfabiovalente@gmail.com",
    "image": "img/Image.png",
    "github_url": "https://github.com/Ediko-eng",
    "linkedin_url": "https://www.linkedin.com/in/edmilson-fabio-valente-297687310/",
    "facebook_url": "https://www.facebook.com/share/1C5Vf6E44g/?mibextid=wwXIfr",
    "instagram_url": "https://www.instagram.com/invites/contact/?igsh=pwoztob2i0l7&utm_content=ok4ruiu",
    "github_handle": "@Ediko-eng",
    "facebook_handle": "@edmilson.fabio",
    "instagram_handle": "@edmilson.dev",
    "linkedin_label": "Edmilson Fabio Valente",
    "knows_about": "Web Development, Machine Learning, Deep Learning, Python",
}

SKILLS = [
    ("Frontend", "HTML, CSS, JavaScript, React", "fas fa-code", 1),
    ("Backend", "PHP, Python, Django, Node.js", "fas fa-server", 2),
    ("Database", "PostgreSQL, MySQL, MongoDB", "fas fa-database", 3),
    ("ML/DL", "TensorFlow, PyTorch, scikit-learn", "fas fa-brain", 4),
]

PROJECTS = [
    {
        "title": "Tetum Morphology Detection",
        "description": "A tool to detect and analyze Tetum language morphology – built as "
        "part of my research at UNTL.",
        "icon": "fas fa-language",
        "github_url": "https://github.com/Ediko-eng/Edmilson-Fabio-Valente.git",
        "tech": "Python, NLP",
        "order": 1,
    },
    {
        "title": "Quiz: How to be a Millionaire",
        "description": 'Desktop quiz game built with PyQt6 – test your knowledge in this '
        '"Who Wants to Be a Millionaire?" style game.',
        "icon": "fas fa-gamepad",
        "github_url": "https://github.com/Ediko-eng/Quiz-How-to-be-a-Millionare.git",
        "tech": "Python, PyQt6",
        "order": 2,
    },
    {
        "title": "HIV/AIDS Data Analysis",
        "description": "Analysis of HIV/AIDS quantitative indicators in Timor-Leste, "
        "segmented by sex – using Python and data science libraries.",
        "icon": "fas fa-chart-bar",
        "github_url": "https://github.com/Ediko-eng/Data-Scince.git",
        "tech": "Python, Pandas, Data Science",
        "order": 3,
    },
    {
        "title": "Sign Language Classification",
        "description": "Machine learning model using K-Nearest Neighbors to classify hand "
        "signs for sign language recognition.",
        "icon": "fas fa-hand-paper",
        "github_url": "https://github.com/Ediko-eng/SIGNLANGUAGE-CLASSIFICATION.git",
        "tech": "Python, scikit-learn, KNN",
        "order": 4,
    },
    {
        "title": "Notes App (Android)",
        "description": "Secure & minimalist note-taking system for Android, built with "
        "Kotlin and Jetpack components. Fast, responsive, and optimized for seamless "
        "productivity.",
        "icon": "fas fa-mobile-alt",
        "github_url": "https://github.com/Ediko-eng/Notes",
        "tech": "Kotlin, Android, Jetpack",
        "order": 5,
    },
    {
        "title": "Calculator App",
        "description": "Clean, modern web calculator supporting basic arithmetic "
        "operations. Built with HTML, CSS, and JavaScript for a smooth and intuitive user "
        "experience.",
        "icon": "fas fa-calculator",
        "github_url": "https://github.com/Ediko-eng/calculator-app/tree/main",
        "tech": "HTML, CSS, JavaScript",
        "order": 6,
    },
    {
        "title": "Date Agenda",
        "description": "Organized scheduling and planning app for managing dates, tasks, "
        "and personal commitments efficiently.",
        "icon": "fas fa-calendar-check",
        "github_url": "https://github.com/Ediko-eng/Date-Agenda",
        "tech": "",
        "order": 7,
    },
]


class Command(BaseCommand):
    help = "Populate the database with the portfolio's current content."

    def handle(self, *args, **options):
        self._seed_profile()
        self._seed_skills()
        self._seed_projects()
        self.stdout.write(self.style.SUCCESS("Portfolio content seeded."))

    def _seed_profile(self):
        profile = Profile.load() or Profile()
        for field, value in PROFILE.items():
            setattr(profile, field, value)
        profile.save()

    def _seed_skills(self):
        for title, description, icon, order in SKILLS:
            Skill.objects.update_or_create(
                title=title,
                defaults={
                    "description": description,
                    "icon": icon,
                    "order": order,
                },
            )

    def _seed_projects(self):
        for data in PROJECTS:
            Project.objects.update_or_create(
                title=data["title"],
                defaults=data,
            )
