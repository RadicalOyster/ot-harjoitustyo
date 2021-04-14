from invoke import task

@task
def start(ctx):
    try:
        ctx.run("python3 src/index.py")
    except:
        ctx.run("python src/index.py")