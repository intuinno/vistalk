from celery import Celery
celery = Celery()

@celery.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    celery.worker.main()

