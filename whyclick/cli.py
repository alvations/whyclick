# -*- coding: utf-8 -*-

import click

from whyclick.chrome import open_chrome, remove_popups
from whyclick import whyq

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def cli():
    pass


@cli.command("download-whyq-orders")
@click.option(
    "--username", "-u", help="Your WhyQ username."
)
@click.option(
    "--password", "-p", help="Your WhyQ password."
)
def download_whyq_orders(
    username,
    password
):
    # Login to WhyQ
    driver = whyq.login(username, password)
    # Extract previous order.
    orders_json = whyq.download_previous_orders(driver)
    # Prints out the json.
    with click.get_text_stream("stdout") as fout:
        print(orders_json, file=fout)


@cli.command("randomly-order-whyq")
@click.option(
    "--username", "-u", help="Your WhyQ username."
)
@click.option(
    "--password", "-p", help="Your WhyQ password."
)
@click.option(
    "--halal", is_flag=True, default=False, help="Halal only options."
)
@click.option(
    "--healthy", is_flag=True, default=False, help="Healthy only options."
)
@click.option(
    "--vegetarian", is_flag=True, default=False, help="Vegetarian only options."
)
def randomly_order_whyq(
    username,
    password,
    halal,
    healthy,
    vegetarian
):
    # Login to WhyQ
    driver = whyq.login(username, password)
    # Randomly order.
    whyq.randomly_order(driver, halal, healthy, vegetarian)
