/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

import { getConfig_nimbusConfig_outcomes } from "../types/getConfig";

export type OutcomeSlugs = (string | null)[] | null;
export type Outcome = getConfig_nimbusConfig_outcomes | null | undefined;
export type OutcomesList = Outcome[];
export type ReviewReadiness = {
  ready: boolean;
  invalidPages: string[];
  missingFields: string[];
  isMissingField: (fieldName: string) => boolean;
  refetch: () => void;
};
