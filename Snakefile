rule prepare:
    output:
        "data/cardata.csv"
    shell:
        "python prepare_data.py"

rule profile:
    input:
        "data/cardata.csv"
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"

rule analysis:
    input:
        "data/cardata.csv"
    output:
        "results/buying_distribution.png"
    shell:
        "scripts/analysis.py"

rule reproduce:
    input:
        "results/buying_distribution.png",
        "profiling/report.html"
