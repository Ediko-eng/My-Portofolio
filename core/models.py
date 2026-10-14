from django.db import models


class Profile(models.Model):
    """Single-row model holding the portfolio owner's details."""

    name = models.CharField(max_length=120, default="Edmilson Fabio Valente")
    logo_text = models.CharField(max_length=40, default="E.V.Dev")
    job_title = models.CharField(
        max_length=120, default="Web Developer & ML/AI Enthusiast"
    )
    subtitle = models.CharField(
        max_length=200,
        default="Informatics Engineering student · Web developer · ML/AI enthusiast",
    )
    about = models.TextField(
        help_text="Separate paragraphs with a blank line."
    )
    university = models.CharField(
        max_length=160, default="UNTL · Informatics Engineering"
    )
    email = models.EmailField(default="edmilsonfabiovalente@gmail.com")
    image = models.CharField(
        max_length=200,
        default="img/Image.png",
        help_text="Path inside the static folder, or a full image URL.",
    )

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    github_handle = models.CharField(max_length=80, blank=True, default="@Ediko-eng")
    facebook_handle = models.CharField(
        max_length=80, blank=True, default="@edmilson.fabio"
    )
    instagram_handle = models.CharField(
        max_length=80, blank=True, default="@edmilson.dev"
    )
    linkedin_label = models.CharField(
        max_length=120, blank=True, default="Edmilson Fabio Valente"
    )

    knows_about = models.CharField(
        max_length=300,
        blank=True,
        default="Web Development, Machine Learning, Deep Learning, Python",
        help_text="Comma-separated topics for the structured data.",
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

    @classmethod
    def load(cls):
        return cls.objects.first()

    @property
    def knows_about_list(self):
        return [item.strip() for item in self.knows_about.split(",") if item.strip()]

    @property
    def social_urls(self):
        return [
            url
            for url in (
                self.github_url,
                self.linkedin_url,
                self.facebook_url,
                self.instagram_url,
            )
            if url
        ]


class Skill(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    icon = models.CharField(
        max_length=80,
        default="fas fa-code",
        help_text="Font Awesome class, e.g. fas fa-code",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(
        max_length=80,
        default="fas fa-folder",
        help_text="Font Awesome class, e.g. fas fa-language",
    )
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True, help_text="Optional live demo link.")
    tech = models.CharField(
        max_length=200,
        blank=True,
        help_text="Comma-separated tech tags, e.g. Python, NLP",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        return [item.strip() for item in self.tech.split(",") if item.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}> — {self.created_at:%Y-%m-%d}"
