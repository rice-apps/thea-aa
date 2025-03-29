<script lang="ts">
	// +page.svelte for /about route
</script>

<main class="p-10">
	<!-- 2-column layout: left = content, right = image -->
	<div class="grid grid-cols-1 items-start gap-8 md:grid-cols-2">
		<!-- 📝 Left Column -->
		<div>
			<h1 class="mb-4 text-3xl font-bold">About This Project</h1>
			<p class="mb-6 max-w-3xl text-lg leading-relaxed">
				This web app maps out Superfund sites and emission events across Texas, making it easier for
				the public to visualize and understand environmental risks in their communities. Instead of
				combing through government spreadsheets and databases, users can now see sites on an
				interactive map, view contaminants present, and explore real-time air quality rankings in
				their area. At its core, the tool is about environmental transparency and accessibility —
				helping individuals, families, and communities stay informed about nearby environmental
				hazards. Data is pulled from public APIs and refreshed regularly, so the map is always up to
				date with the latest information.
			</p>

			<!-- 🧪 Toggle sections -->
			<details class="mb-4">
				<summary class="tex-600 cursor-pointer hover:underline"> 🧪 What is Superfund? </summary>
				<p class="mt-2 text-base leading-relaxed">
					Superfund is a federal EPA program that identifies and cleans up hazardous waste sites
					across the U.S. These sites pose serious health and environmental risks, often due to
					historical dumping of toxic substances. The goal is to safely contain or remove the
					pollution.
				</p>
			</details>

			<details class="mb-4">
				<summary class="text-600 cursor-pointer hover:underline"> 🌬 What is TCEQ? </summary>
				<p class="mt-2 text-base leading-relaxed">
					The Texas Commission on Environmental Quality (TCEQ) oversees environmental regulation in
					Texas, including monitoring air and water quality, managing waste, and reporting
					industrial emission events.
				</p>
			</details>
		</div>

		<!-- 🖼️ Right Column: Picture -->
		<div
			class="flex h-[300px] items-center justify-center border-2 border-red-400 bg-[#003344] text-red-400"
		>
			Picture placeholder
		</div>
	</div>

	<section class="mt-8">
		<h2 class="text-2xl font-semibold">Features</h2>
		<ul class="ml-6 mt-2 list-disc text-base">
			<li>Interactive map with environmental overlays</li>
			<li>Search by location and filter by radius</li>
			<li>Contaminated site + emission event info</li>
			<li>Air quality rankings</li>
		</ul>
	</section>

	<section class="mt-8">
		<h2 class="text-2xl font-semibold">Team</h2>
		<p class="mt-2">
			Developed by
			<a
				href="https://www.riceapps.org"
				class="font-medium text-blue-600 hover:underline"
				target="_blank"
				rel="noopener noreferrer"
			>
				RiceApps
			</a>
		</p>

		<ul class="ml-6 mt-4 list-disc space-y-2 text-base">
			<li>
				<span class="font-medium">Team Leads:</span>
				<ul class="ml-4 list-disc">
					<li>Aiden, Rice '25</li>
				</ul>
			</li>

			<li>
				<span class="font-medium">PM:</span>
				<ul class="ml-4 list-disc">
					<li>Aaron, Rice '26</li>
				</ul>
			</li>

			<li>
				<span class="font-medium">Designer:</span>
				<ul class="ml-4 list-disc">
					<li>Grace, Rice '26</li>
				</ul>
			</li>

			<li>
				<span class="font-medium">Developers:</span>
				<ul class="ml-4 list-disc">
					<li>James, Rice '25</li>
					<li>Nomin, Rice '26</li>
					<li>Vismay, Rice '28</li>
					<li>Iris, Rice '26</li>
					<li>Sanya, Rice '26</li>
					<li>Nam, Rice '28</li>
					<li>Oliver, Rice '28</li>
				</ul>
			</li>
		</ul>
	</section>
</main>
