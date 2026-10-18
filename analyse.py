with open("wards.csv")as f:
    lines=f.readlines()

    print("Number of lines:", len(lines))

    with open("wards.csv")as f:
        lines=f.readlines()

    for line in lines:
        print(line.strip())

        with open("wards.csv") as f:
            lines=f.readlines()

            for line in lines [1:]:
                parts=line.strip().split(",")
                ward=parts[0]
                area=parts[1]
                print(ward,"has area",area)

                with open("wards.csv") as f:
                    lines=f.readlines()

                    for line in lines[1:]:
                        parts=line.strip().split(",")
                        ward=parts[0]
                        area_km2=float(parts[1])
                        area_hectares=area_km2*100
                        print(ward,"is",area_hectares,"hectares")

                with open("wards.csv") as f:
                    lines=f.readlines()
                        
                    for line in lines[1:]:
                        parts=line.strip().split(",")
                        ward=parts[0]
                        area_km2=float(parts[1])
                        if area_km2>9:
                           size="large"
                        else:
                            size="small"
                        print(ward,"is",size)