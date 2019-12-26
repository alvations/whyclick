# whyclick

Cos I don't like clicking...

# Install

```
pip install -U whyclick
```


# Usage

## Randomly orders for the week

```
$ whyclick randomly-order-whyq --help
Usage: whyclick randomly-order-whyq [OPTIONS]

Options:
  -u, --username TEXT  Your WhyQ username.
  -p, --password TEXT  Your WhyQ password.
  --halal              Halal only options.
  --healthy            Healthy only options.
  --vegetarian         Vegetarian only options.
  -h, --help           Show this message and exit.

$ whyclick randomly-order-whyq \
-u alvas@xmail.com -p ****
```

## Download your previous orders

```
$ whyclick download-whyq-orders --help
Usage: whyclick download-whyq-orders [OPTIONS]

Options:
  -u, --username TEXT  Your WhyQ username.
  -p, --password TEXT  Your WhyQ password.
  -h, --help           Show this message and exit.

$ whyclick download-whyq-orders \
-u alvas@xmail.com -p **** > whyq-myorders.json

$ cat whyq-myorders.json
```
