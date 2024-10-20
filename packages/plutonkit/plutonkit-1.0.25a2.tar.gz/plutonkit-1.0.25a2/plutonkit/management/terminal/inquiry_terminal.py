class InquiryTerminal:
    def __init__(self, choices) -> None:
        self.ref_answer = {}
        self.choices = choices
        self.var_is_continue = True
        self.var_is_terminate = False

    def execute(self):
        if len(self.choices) > 0:
            self._selection(self.choices)
        else:
            self.var_is_terminate = True

    def get_answer(self):
        return self.ref_answer

    def is_continue(self):
        return self.var_is_continue

    def is_terminate(self):
        return self.var_is_terminate

    def _selection(self, choices):
        choice = choices[0]

        name = choice.get("name", "")
        question = choice.get("question", "")
        type_choice = choice.get("type", "")
        default = choice.get("default", "")

        if type_choice == "input":
            question = input(f"{question}?:")
            if question == "":
                question = default
            self.ref_answer[name] = question
            choices.pop(0)
        if type_choice == "single_choice":
            option = choice.get("option", [])

            enum_action = [f"[{key+1}] {val}" for key, val in enumerate(option)]
            join_enum_action = "\n".join(enum_action)
            print(f"\n{question}\n{join_enum_action} ")
            try:
                options_ans = "1" if len(option) == 1 else "1-" + str(len(option))
                answer = input(f"choose only at [{options_ans}]")

                available_step = option[int(answer) - 1]
                self.ref_answer[name] = available_step
                choices.pop(0)
            except:
                print("Invalid option, try again")
                self._selection(choices)

        if type_choice == "multiple_choice":
            option = choice.get("option", [])

            enum_action = [f"[{key+1}] {val}" for key, val in enumerate(option)]
            join_enum_action = "\n".join(enum_action)
            print(f"\n{question}\n{join_enum_action} (use comma `,` for multiple selection)")
            try:
                answer_multiple_choices = "1" if len(option) == 1 else "1-" + str(len(option))
                answer = input(f"choose only at [{answer_multiple_choices}]")

                self.ref_answer[name] = ""
                answer_split = answer.split(",")
                for kk in answer_split:
                    available_step = option[int(kk) - 1]

                self.ref_answer[name] = answer
                choices.pop(0)
            except:
                print("Invalid option, try again")
                self._selection(choices)

        if len(choices) > 0:
            self._selection(choices)
        else:
            self.var_is_terminate = True
