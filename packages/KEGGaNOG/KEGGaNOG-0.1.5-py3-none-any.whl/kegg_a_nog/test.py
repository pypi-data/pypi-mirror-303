import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
import re
import subprocess
import csv


function_groups = {
    "Carbon Metabolism": [
        "glycolysis",
        "gluconeogenesis",
        "TCA Cycle",
        "RuBisCo",
        "CBB Cycle",
        "rTCA Cycle",
        "Wood-Ljungdahl",
        "Entner-Doudoroff Pathway",
    ],
    "Oxidative Phosphorylation": [
        "NAD(P)H-quinone oxidoreductase",
        "NADH-quinone oxidoreductase",
        "Na-NADH-ubiquinone oxidoreductase",
        "F-type ATPase",
        "V-type ATPase",
        "Cytochrome c oxidase",
        "Ubiquinol-cytochrome c reductase",
        "Cytochrome o ubiquinol oxidase",
        "Cytochrome aa3-600 menaquinol oxidase",
        "Cytochrome c oxidase, cbb3-type",
        "Cytochrome bd complex",
    ],
    "Sulfur and Nitrogen Metabolism": [
        "ammonia oxidation (amo/pmmo)",
        "hydroxylamine oxidation",
        "nitrite oxidation",
        "dissimilatory nitrate reduction",
        "DNRA",
        "nitrite reduction",
        "nitrogen fixation",
        "sulfide oxidation",
        "sulfite dehydrogenase",
        "DMSP demethylation",
        "sulfur disproportionation",
    ],
    "Hydrogen and Redox Metabolism": [
        "NiFe hydrogenase",
        "ferredoxin hydrogenase",
        "hydrogen:quinone oxidoreductase",
        "NAD-reducing hydrogenase",
        "NADP-reducing hydrogenase",
        "NiFe hydrogenase Hyd-1",
    ],
    "Amino Acid Metabolism": [
        "histidine",
        "arginine",
        "lysine",
        "serine",
        "threonine",
        "asparagine",
        "glutamine",
        "cysteine",
        "glycine",
        "proline",
        "alanine",
        "valine",
        "methionine",
        "phenylalanine",
        "isoleucine",
        "leucine",
        "tryptophan",
        "tyrosine",
        "aspartate",
        "glutamate",
    ],
    "Bacterial Secretion Systems": [
        "Type I Secretion",
        "Type II Secretion",
        "Type III Secretion",
        "Type IV Secretion",
        "Type Vabc Secretion",
        "Type VI Secretion",
        "Sec-SRP",
        "Twin Arginine Targeting",
    ],
    "Biofilm Formation and Motility": [
        "Flagellum",
        "Chemotaxis",
        "Biofilm PGA Synthesis protein",
        "Colanic acid biosynthesis",
        "Adhesion",
        "Competence-related core components",
        "Competence-related related components",
    ],
    "Transporters": [
        "transporter: urea",
        "transporter: phosphate",
        "transporter: phosphonate",
        "transporter: vitamin B12",
        "transporter: thiamin",
        "Cobalt transporter CbiMQ",
        "Nickel ABC-type transporter NikA",
        "Copper transporter CopA",
        "Ferrous iron transporter FeoB",
        "Ferric iron ABC-type transporter AfuA",
        "Fe-Mn transporter MntH",
    ],
    "Miscellaneous Pathways": [
        "Methanogenesis via methanol",
        "Methanogenesis via acetate",
        "Photosystem II",
        "Photosystem I",
        "Retinal biosynthesis",
        "Mixed acid: Lactate",
        "Mixed acid: Formate",
        "Naphthalene degradation to salicylate",
        "Polyhydroxybutyrate synthesis",
        "Carotenoid biosynthesis",
        "Arsenic reduction",
    ],
}


# Function to parse eggnog-mapper output and prepare for KEGG-Decoder
def parse_emapper(input_file, temp_folder):
    # Read the input file
    df_filtered = pd.read_csv(input_file, sep="\t", skiprows=4)

    # Extract the 'KEGG_ko' column and clean it up
    df_kegg_ko = df_filtered[["KEGG_ko"]]
    df_kegg_ko = df_kegg_ko[df_kegg_ko["KEGG_ko"] != "-"]

    # Format the 'KEGG_ko' column for KEGG-Decoder
    df_kegg_ko["KEGG_ko"] = df_kegg_ko["KEGG_ko"].str.replace(
        r"ko:(K\d+)", r"SAMPLE \1", regex=True
    )
    df_kegg_ko["KEGG_ko"] = df_kegg_ko["KEGG_ko"].str.replace(",", "\n")

    # Save the parsed file with potential quotes
    parsed_file = os.path.join(temp_folder, "parsed.txt")
    df_kegg_ko.to_csv(
        parsed_file,
        sep="\t",
        index=False,
        header=False,
        quoting=csv.QUOTE_MINIMAL,
        escapechar="\\",
    )

    # Remove all quotation marks from the parsed file
    parsed_filtered_file = os.path.join(temp_folder, "parsed_filtered.txt")
    with open(parsed_file, "r") as file:
        content = file.read()

    # Replace any quotation marks
    content = content.replace('"', "")

    # Write the cleaned content to the parsed_filtered.txt file
    with open(parsed_filtered_file, "w") as file:
        file.write(content)

    return parsed_filtered_file


# Function to run KEGG-Decoder and process the output
def run_kegg_decoder(input_file, temp_folder):
    output_file = os.path.join(temp_folder, "output.list")

    # Run KEGG-Decoder via subprocess
    subprocess.run(
        ["KEGG-decoder", "-i", input_file, "-o", output_file, "-v", "static"]
    )

    return output_file


# Function to generate the heatmap
def generate_heatmap(kegg_decoder_file, output_folder, dpi, sample_name):
    # Read the KEGG-Decoder output
    with open(kegg_decoder_file, "r") as file:
        lines = file.readlines()

    # Prepare the dataframe
    header = lines[0].strip().split("\t")
    values = lines[1].strip().split("\t")
    data = {"Function": header[1:], sample_name: [float(v) for v in values[1:]]}
    df = pd.DataFrame(data)

    # Group the DataFrame by the function_groups
    group_names = []
    group_indices = []

    for group_name, functions in function_groups.items():
        for function in functions:
            if function in df["Function"].values:
                group_names.append(group_name)
                group_indices.append(df["Function"].tolist().index(function))

    # Create a new DataFrame with the group names
    df_grouped = df.iloc[group_indices].copy()
    df_grouped["Group"] = group_names

    # Set the Group as the index to create a multi-index DataFrame
    df_grouped.set_index(["Group", "Function"], inplace=True)

    # Create a grid for the heatmap and colorbar
    fig, ax = plt.subplots(
        figsize=(10, 12)
    )  # Adjusted figure size for better readability
    cbar_ax = fig.add_axes([0.92, 0.4, 0.02, 0.2])  # Colorbar axis on the right

    # Create the heatmap
    sns.heatmap(
        df_grouped.unstack(level=0).fillna(0),
        cmap="Blues",
        annot=True,
        linewidths=0.5,
        ax=ax,
        cbar_ax=cbar_ax,
    )

    # Customize the plot
    ax.set_title(f"Heatmap for {sample_name}")
    ax.set_ylabel("Function")
    ax.set_xlabel("Metabolic Groups")

    # Set layout and save the figure
    plt.tight_layout(rect=[0, 0, 0.9, 1])
    output_file = os.path.join(output_folder, "heatmap_figure.png")
    plt.savefig(output_file, dpi=dpi, bbox_inches="tight")
    plt.show()


# Main function to run the tool
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="KEGGaNOG: Link eggnog-mapper and KEGG-Decoder for pathway visualization."
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Path to eggnog-mapper output file"
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Output folder to save results"
    )
    parser.add_argument(
        "-dpi",
        "--dpi",
        type=int,
        default=300,
        help="DPI for the output image (default: 300)",
    )
    parser.add_argument(
        "-n",
        "--name",
        default="SAMPLE",
        help="Sample name for labeling (default: SAMPLE)",
    )

    args = parser.parse_args()

    # Create output and temporary directories
    os.makedirs(args.output, exist_ok=True)
    temp_folder = os.path.join(args.output, "temp_files")
    os.makedirs(temp_folder, exist_ok=True)

    # Step 1: Parse eggnog-mapper output
    parsed_filtered_file = parse_emapper(args.input, temp_folder)

    # Step 2: Run KEGG-Decoder
    kegg_decoder_file = run_kegg_decoder(parsed_filtered_file, temp_folder)

    # Step 3: Generate the heatmap
    generate_heatmap(kegg_decoder_file, args.output, args.dpi, args.name)

    print(f"Heatmap saved in {args.output}/heatmap_figure.png")


if __name__ == "__main__":
    main()
