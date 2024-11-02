<script lang="ts">
  type Props = {
    name: string
    hazardLevel: number
    regionId: number
    status: string
    location: string
    background: string
    update: ()=>void,
  }

  import { ChevronRight } from "lucide-svelte"
  import { ChevronLeft } from "lucide-svelte"

  let props: { superFundInfo: Props } = $props()
</script>

<article class="w-[30rem] rounded-lg flex flex-col h-[30rem] gap-3 p-5 bg-white">
  <h3 class="flex">
    <btn onclick={()=>{props.superFundInfo.update()}} href="#" class="cursor-pointer">
      <ChevronLeft/>
    </btn> 
    <div class="ml-10">{props.superFundInfo.name}</div>
  </h3>

  <div class="flex gap-10">
    {#each [["Hazard Level", "hazardLevel"], ["Region Id", "regionId"], ["Status", "status"]] as info}
      <div>
        <h5>{info[0]}</h5>
        {props.superFundInfo[info[1]]}
      </div>
    {/each}
  </div>

  <div>
    <h5>Location</h5>
    {props.superFundInfo.location}
  </div>

  <div class="grow">
    <h4>Background</h4>
    <p>{props.superFundInfo.background}</p>
  </div>


  <a href="#" class="mx-5 bg-blue-200 rounded-lg p-2 flex justify-center gap-1">
      <div class="">Learn more</div> 
      <ChevronRight/>
  </a>
</article>