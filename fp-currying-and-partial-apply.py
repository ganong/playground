from celery import chain, group
from bandwdth_be.celery import celery_app

@celery_app.task(name="demo.do_stuff")
def do_stuff(a, b, c):
    pass

a = "foo"
b = "bar"
c = "baz"

do_stuff.apply_async((a,b,c))
do_stuff.delay(a,b,c)
do_stuff(a, b, c)

ds_sig = do_stuff.signature() # mirrors apply_async
ds_sig.apply_async((a, b, c))

ds_s = do_stuff.s() # mirrors delay
ds_s.delay()

ds = do_stuff.s(a, b)
ds.delay(c)

ds_all = do_stuff.s(a, b, c)
ds_all.delay()


# s vs si
#immutable=True

ds_signature_imm = do_stuff.signature((a, b, c), immutable=True)
ds_signature_imm()

ds1 = do_stuff.si(a, b, c)
ds2 = do_stuff.si(a, c, b)
ds3 = do_stuff.si(a, b, c)

ds1 = do_stuff.s(a, b, c)
ds2 = do_stuff.s(c, b, a)
ds3 = do_stuff.s(b, a, c)

ch = chain(ds1, ds2, ds3)

ch()
ch.delay()
ch.apply_async()

g = group(ds1, ds2, ds3)

g()
g.delay()
g.apply_async()

g2 = group(ds2, ds3)

ch2 = chain(g, g2, ds1)

ch2.delay()







from functools import partial

def add(a,b,c):
    pass

p = partial(add, 1, 2)

p(3)

p2 = partial(add, c=3, b=2)

p2(1)
