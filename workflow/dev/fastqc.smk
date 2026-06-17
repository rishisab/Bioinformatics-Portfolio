configfile: "config/config.yaml"

SAMPLES = config["samples"]

rule all:
    input:
        expand("results/fastqc/{sample}_{read}_fastqc.html",
               sample=SAMPLES,
               read=["R1", "R2"])

rule fastqc:
    input:
        "data/raw/{sample}_{read}.fastq.gz"
    output:
        "results/fastqc/{sample}_{read}_fastqc.html"
    shell:
        """
        mkdir -p results/fastqc
        fastqc {input} -o results/fastqc/
        """
