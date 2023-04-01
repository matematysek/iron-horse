from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="nemesis",
        base_numeric_id=6750,
        name="Nemesis",
        role="super_heavy_express",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2900,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=10,  # let's be later for this one
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=60, vehicle_length=6, repeat=2
    )

    consist.description = """Good horses make short miles."""
    consist.foamer_facts = """Irish Railways 181 Class"""

    return consist