#!/bin/bash

reload(){
    curl -L https://github.com/ionet-official/io_launch_binaries/raw/main/launch_binary_mac -o launch_binary_mac
    chmod +x launch_binary_mac
    ./launch_binary_mac --device_id=x --user_id=x --operating_system="macOS" --usegpus=false --device_name=x
}

# List of container names
container_imgs=("io-worker-vc" "io-worker-monitor")

while true
do

    trigger=1

    ############################# Check container count ########################################
    ############################################################################################
    container_count=$(docker ps -q | wc -l)

    if [ $container_count -le 1 ] 
    then
        echo "container amount is less than 2"
        trigger=$((trigger*0))
    fi

    ############################# Check container images #######################################
    ############################################################################################

    # Get a list of running container IDs
    container_ids=$(docker ps -q)

    # Iterate through each container

    has_img=0

    for container_id in $container_ids
    do
        # Get the image name associated with the container
        container_image=$(docker inspect --format '{{.Config.Image}}' "$container_id")

        # Check if the image name contains the target string
        
        for img in "${container_imgs[@]}"
        do          
            if [[ "$container_image" == *"$img"* ]]
            then
                echo "Container matched '$img'."
                has_img=$((has_img+1))
            fi
        done

    done

    if [ $has_img -lt 2 ]
    then
        trigger=$((trigger*0))
    fi

    if [ $trigger -eq 0 ]
    then
        echo "run reload method"
        reload
    else
        echo "container is normal"
    fi

    #Set up timer

    countdown=60
    while (($countdown>0))
    do
        echo "container status will be checked after $countdown minutes"
        countdown=$((countdown-10))
        sleep 600
    done

    sleep 3600

done
