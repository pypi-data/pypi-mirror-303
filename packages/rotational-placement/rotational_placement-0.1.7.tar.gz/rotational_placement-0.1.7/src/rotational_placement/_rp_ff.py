def _rp_ff(a: int, b: int, step_size: int, max_radius: int, experiment) -> dict[str,float]:
    import numpy as np

    PI = np.pi
    ROTATIONAL_FACTOR = a / b
    RADIUS_EVENT_HORIZON = 1 / np.sin(PI / b)

    def __add_segment(a: int, b: int, segments:list[dict[str,float]]):
        
        number_of_arcs = 1

        arc_angle = 2 * PI * ((number_of_arcs * ROTATIONAL_FACTOR) % 1)

        if arc_angle > PI:
            arc_angle = 2 * PI - arc_angle

        while arc_angle > 2 * np.arcsin(1 / segments[-1]["segment_radius"]):
            number_of_arcs += 1
            arc_angle = 2 * PI * ((number_of_arcs * ROTATIONAL_FACTOR) % 1)

            if arc_angle > PI:
                arc_angle = 2 * PI - arc_angle

        segment_radius = 2 / np.sin(arc_angle)
        arc_quotient = ((segment_radius + 1) * (segment_radius + 1) - (segment_radius - 1) * (segment_radius - 1) + ((segment_radius * np.sin(np.pi / number_of_arcs)) * np.sin(np.pi / number_of_arcs))) / ((2 * segment_radius * np.sin(np.pi / number_of_arcs)) * (segment_radius + 1))
        arc_span = np.arccos(arc_quotient) + PI / 2
        seeds_per_arc = np.round(arc_span / 2 * arc_angle)

        segment = {
            "number_of_arcs":number_of_arcs,
            "arc_angle":arc_angle,
            "segment_radius":segment_radius,
            "arc_quotient":arc_quotient,
            "arc_span":arc_span,
            "seeds_per_arc":seeds_per_arc,
            "segment_efficacy":seeds_per_arc * number_of_arcs
        }        

        return segment
    
    def __truncate_segment(current_segment:dict[str,float], previous_segment:dict[str,float], current_radius:int):
        reduction_angle = 2 * np.arcsin(previous_segment['segment_radius'] / current_segment["segment_radius"])
        truncation_angle = 2 * np.arcsin(current_radius / current_segment["segment_radius"])

        truncated_seeds = round((truncation_angle - reduction_angle) / (2 * current_segment["arc_angle"]))

        return truncated_seeds


    #create segments up until max_radius
    segments = [{"segment_radius":2, "segment_efficacy": 1}]

    if max_radius < RADIUS_EVENT_HORIZON: 
        while segments[-1]["segment_radius"] < max_radius: 
            segments.append(__add_segment(a,b,segments))
    else: 
        while segments[-1]["segments_radius"] < RADIUS_EVENT_HORIZON:
            segments.append(__add_segment(a,b,segments))
            
        segment = {
            "number_of_arcs":b,
            "arc_angle":0,
            "segment_radius":max_radius,
            "arc_quotient":((max_radius + 1)**2-(max_radius - 1)**2 + (max_radius * np.sin(np.pi / max_radius))**2) / ((2 * max_radius * np.sin(np.pi / max_radius)) * (max_radius + 1)),
            "arc_span":max_radius,
            "seeds_per_arc": (max_radius - segments[-1]['segmentRadius']) / 2
        }
        
        segments.append(segment)

    #collect data and return it
    data_dict = {"radius":[],"efficacy":[]}

    for current_radius in (2, max_radius, step_size):

        for i, segment in enumerate(segments):

            if segment["segment_radius"] > current_radius:
                efficacy = 0
                for segment in segments[:i]:
                    efficacy += segment["segment_radius"]
                efficacy += __truncate_segment(segments[i],segments[i-1],current_radius)
                break
        
        data_dict["radius"].append(current_radius)
        data_dict["efficacy"].append(efficacy)

    return data_dict