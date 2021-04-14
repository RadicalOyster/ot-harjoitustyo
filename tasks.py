from invoke import task

@task
def start(ctx):
    try:
        ctx.run("python3 src/index.py")
    except:
        ctx.run("python src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src")