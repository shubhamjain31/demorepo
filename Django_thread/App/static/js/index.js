var upload = new FileUploadWithPreview("myUniqueUploadId");
        var current_count_for_skills = 0

        function addInputForSkills(){


            var html = ` 
            <div class="row mt-3" id="input_skill_${current_count_for_skills}"> 
            <div class="form-group col-md-8">
                    <label>Add Skills</label>
                    <input class="form-control" required name="skills" type="text" placeholder="Enter Skills">
                </div>
                <div class="form-group col-md-4 mt-4">
                    <button type="button" onclick="removeSkillInput(${current_count_for_skills})" class="btn btn-danger" id>Delete</button>
                </div>
                </div>`

            document.getElementById('skill_row').innerHTML += html

            current_count_for_skills++
        }

        function removeSkillInput(id) {

            var element = document.getElementById(`input_skill_${id}`);
            element.remove()

        }
