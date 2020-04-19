#!/usr/bin/env bash
docker_info=$(lbs alb-instance-list -a | grep albins- | awk -F '|' '{print $3 $4 $7 $13}')
echo $docker_info
docker_infos=(${docker_info// / })
echo ${#docker_infos[@]}
echo "---------------------------------------------------------------"

i=0
while (($i < $(expr ${#docker_infos[@]} / 4))); do
  tenant_id=${docker_infos[4 * i]}
  subnet_id=${docker_infos[4 * i + 1]}
  alb_id=${docker_infos[4 * i + 2]}
  docker_id=${docker_infos[4 * i + 3]}
  jvirt_tenant_id=$(jvirt container-show $docker_id -a | grep user_id | awk -F '|' '{print $3}' | sed 's/ //g')
  subnet_tenant_id=$(ccs subnet-show $subnet_id -a | grep tenant_id | awk -F '|' '{print $3}' | sed 's/ //g')
  alb_tenant_id=$(lbs lb-show $alb_id -a | grep TenantId | awk -F '|' '{print $3}' | sed 's/ //g')
  if [[ (${tenant_id} != ${jvirt_tenant_id}) || ($tenant_id != ${subnet_tenant_id}) || ($alb_tenant_id != ${tenant_id}) ]]; then
    echo "tenant_id not equal, ${alb_id}, ${docker_id}, ${tenant_id}, ${jvirt_tenant_id}, ${subnet_tenant_id}, ${alb_tenant_id}"
  fi
  i=`expr ${i} + 1`
  mod=`expr $i % 100`
  if [[ $mod -eq 0 ]]; then
    sleep 5
  fi
done
