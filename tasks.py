from invoke import task
import os

@task
def start(ctx):
    if (os.name == "nt"):
        ctx.run("python src/index.py")
    else: 
        ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src")