import uuid

import typer

from .backend_client.gen.models import Report
from .backend_client.client import TheCVESBackend
from .settings import TheCvesSettings


app = typer.Typer()
the_cves_cli_settings = TheCvesSettings()
backend_client = TheCVESBackend(the_cves_cli_settings)


@app.command("run_report")
def run_report(product_id: int, release_id: int, confluence_space_key: str, image_id: int = None, cve: str = None,
               confluent_parent_page_title: str = None):
    """
    Generate a report for a given product and release.

    Args:
        :param product_id: The product ID (mandatory).
        :param release_id: The release ID (mandatory).
        :param image_id: The image ID.
        :param cve: The CVE.
        :param confluence_space_key: the confluence space key
        :param confluent_parent_page_title:
        :param github_token:
        :param github_repo_url:
    """
    typer.echo(
        f"Generating report for product_id: {product_id}, release_id: {release_id}, image_id: {image_id}, cve: {cve}."
        f"Writing to confluence domain: {the_cves_cli_settings.confluence_domain}.")
    res: Report = backend_client.start_job(Report(productID=product_id, releaseID=release_id,
                                                  imageID=image_id, cve=cve, confluenceSpaceKey=confluence_space_key,
                                                  confluenceKey=the_cves_cli_settings.confluence_token,
                                                  confluenceDomain=the_cves_cli_settings.confluence_domain,
                                                  confluenceUser=the_cves_cli_settings.confluence_user,
                                                  confluenceParentPageTitle=confluent_parent_page_title,
                                                  gitHubToken=the_cves_cli_settings.github_token,
                                                  gitHubRepoURL=the_cves_cli_settings.github_repo_url))
    typer.echo(f"Job ID: {res.id}, Confluence page URL: {res.docURL}")


@app.command("status")
def status(job_id: uuid.UUID):
    """
    Generate a report for a given product and release.

    Args:
        job_id (str): The job_id ID (mandatory).
    """
    typer.echo(
        f"Getting status for job_id: {job_id}")
    report: Report = backend_client.get_status(job_id)
    typer.echo(f"Status: {report.status}, Confluence page URL: {report.docURL}")


if __name__ == "__main__":
    app()
